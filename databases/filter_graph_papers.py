#!/usr/bin/env python3
"""
Filter arXiv papers by specific categories related to graph theory and network science.

Target categories:
- math.CO: Mathematics - Combinatorics
- cs.DM: Computer Science - Discrete Mathematics
- physics.soc-ph: Physics - Physics and Society
- cs.DS: Computer Science - Data Structures and Algorithms
- stat.ML: Statistics - Machine Learning
- q-bio.MN: Quantitative Biology - Molecular Networks
- cond-mat.stat-mech: Condensed Matter - Statistical Mechanics
"""

import json
import sys
from datetime import datetime

# Define target categories (including both old and new arXiv category formats)
TARGET_CATEGORIES = {
    'math.CO',           # Combinatorics
    'cs.DM',             # Discrete Mathematics
    'physics.soc-ph',    # Physics and Society
    'cs.DS',             # Data Structures and Algorithms
    'stat.ML',           # Machine Learning
    'cond-mat.dis-nn',   # Disordered Systems and Neural Networks
    'cond-mat.stat-mech' # Statistical Mechanics
}

def get_user_categories():
    """Prompt user to confirm or modify target categories."""
    print("Default categories:")
    default_cats = sorted(TARGET_CATEGORIES)
    for i, cat in enumerate(default_cats, 1):
        print(f"  {i}. {cat}")

    print("\nOptions:")
    print("  - Press ENTER to use default categories")
    print("  - Type category names separated by commas to use custom categories")
    print("    (e.g., math.CO,cs.DM,physics.soc-ph)")

    user_input = input("\nYour choice (press ENTER for defaults): ").strip()

    if not user_input:
        return TARGET_CATEGORIES

    # Parse custom categories
    custom_cats = {cat.strip() for cat in user_input.split(',') if cat.strip()}
    return custom_cats if custom_cats else TARGET_CATEGORIES

def get_from_date():
    """Prompt user for the from date filter."""
    print("\nEnter the earliest date for papers (YYYY-MM-DD format):")
    print("  Press ENTER to include all dates")

    while True:
        user_input = input("From date: ").strip()

        if not user_input:
            return None

        try:
            # Validate date format
            datetime.strptime(user_input, '%Y-%m-%d')
            return user_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD (e.g., 2020-01-01)")

def get_keyword_filters():
    """Prompt user for optional keyword filters."""
    print("\nOptional keyword filters:")
    print("  Leave empty to match all papers")

    title_keyword = input("Keyword to search in title: ").strip().lower()
    abstract_keyword = input("Keyword to search in abstract: ").strip().lower()

    return title_keyword if title_keyword else None, abstract_keyword if abstract_keyword else None

def matches_categories(categories_str, target_categories):
    """Check if any target category appears in the categories string."""
    if not categories_str:
        return False

    # Split by space to get individual categories
    categories = categories_str.split()

    # Check if any target category is present
    return any(cat in target_categories for cat in categories)

def matches_date(update_date, from_date):
    """Check if paper's update date is on or after the from_date."""
    if not from_date:
        return True

    if not update_date:
        return False

    # Extract date portion (YYYY-MM-DD) from the update_date string
    paper_date = update_date.split()[0] if ' ' in update_date else update_date
    return paper_date >= from_date

def matches_keywords(paper, title_keyword, abstract_keyword):
    """Check if paper matches the keyword filters (case-insensitive, partial match)."""
    if title_keyword:
        title = paper.get('title', '').lower()
        # Check if keyword appears anywhere in the title
        if title_keyword not in title:
            return False

    if abstract_keyword:
        abstract = paper.get('abstract', '').lower()
        # Check if keyword appears anywhere in the abstract
        if abstract_keyword not in abstract:
            return False

    return True

def filter_papers(input_file, output_file, target_categories, from_date, title_keyword, abstract_keyword):
    """Filter papers from input JSON file and write matching ones to output file."""
    matched_count = 0
    total_count = 0

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile:

        for line in infile:
            total_count += 1

            try:
                paper = json.loads(line.strip())

                # Check if paper matches all criteria
                if (matches_categories(paper.get('categories', ''), target_categories) and
                    matches_date(paper.get('update_date', ''), from_date) and
                    matches_keywords(paper, title_keyword, abstract_keyword)):
                    outfile.write(line)
                    matched_count += 1

            except json.JSONDecodeError as e:
                print(f"Error parsing line {total_count}: {e}", file=sys.stderr)
                continue

            # Progress indicator
            if total_count % 100000 == 0:
                print(f"Processed {total_count} papers, matched {matched_count}...", file=sys.stderr)

    print(f"\nFiltering complete!", file=sys.stderr)
    print(f"Total papers processed: {total_count}", file=sys.stderr)
    print(f"Papers matching criteria: {matched_count}", file=sys.stderr)
    print(f"Percentage: {100 * matched_count / total_count:.2f}%", file=sys.stderr)

if __name__ == '__main__':
    input_file = 'arxiv-metadata-oai-snapshot.json'
    output_file = 'arxiv-graph-theory-filtered.json'

    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    print("=" * 60)
    print("arXiv Paper Filter Configuration")
    print("=" * 60)

    # Get user preferences
    target_categories = get_user_categories()
    from_date = get_from_date()
    title_keyword, abstract_keyword = get_keyword_filters()

    # Display configuration summary
    print("\n" + "=" * 60)
    print("Configuration Summary")
    print("=" * 60)
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")
    print(f"Categories: {', '.join(sorted(target_categories))}")
    print(f"From date: {from_date if from_date else 'All dates'}")
    print(f"Title keyword: {title_keyword if title_keyword else 'None'}")
    print(f"Abstract keyword: {abstract_keyword if abstract_keyword else 'None'}")
    print("=" * 60 + "\n")

    filter_papers(input_file, output_file, target_categories, from_date, title_keyword, abstract_keyword)
