## Sample Datasets for Analysis with InfraNodus

[InfraNodus](https://infranodus.com) is a AI-powered text network analysis tool. You can use it to reveal patterns in text data.

Here we provide some of the sample datasets you can use to try out various workflows.

![InfraNodus network graph](https://infranodus.com/images/front/infranodus-network-analysis-tool-app.webp)

### Keyword Stats

This folder contains the data on Google Search volumes for various keywords. Usually you would analyze the column with the keyword combinations to find recurring patterns and use metadata in other columns for filtering (e.g. search volume, difficulty, location, etc.)

– [Keyword Stats / google_us_ai-tools_matching-terms_2025-07-08_20-05-24.csv](keyword-stats/google_us_ai-tools_matching-terms_2025-07-08_20-05-24.csv): Google Search volumes for keywords related to "ai tools". Use the [matching keyword workflow](https://support.noduslabs.com/hc/en-us/articles/21038197757084-Find-the-Search-Terms-that-Relate-to-a-Search-Query-with-Ahrefs-and-InfraNodus) to see how to analyze this file step by step.

### Open-Ended Surveys

This folder contains samples of open-ended surveys. Usually one or more columns contain the responses while the other columns contain metadata about the survey participants. This metadata can be used for filtering: e.g. what the people from a certain location or background said about a partciular topic or their sentiment.

- [Open Ended Surveys / OSMI-2019-Mental-Health-Tech-Modified.csv](open-ended-surveys/OSMI-2019-Mental-Health-Tech-Modified.csv): Open Source Mental Health Initiative (OSMI) 2019 Mental Health Tech Survey. Use the [open-ended survey workflow](https://support.noduslabs.com/hc/en-us/articles/19917497109020-Qualitative-Analysis-of-Interviews-Open-Ended-Survey-Responses-and-Customer-Feedback) to see how to analyze this file step by step.

### Listings

This folder contains samples of listings. Such listings would often contain a column with a title and description of a listing as well as severeal other columns with categories which can be used for filtering.

- [Listings / ec_europa_data.csv](listings/ec_europa_data.csv): European Commission Open Data Portal. Use the [listings workflow](https://support.noduslabs.com/hc/en-us/sections/7448975794076-Quick-Start-Recommended-Workflows) to see how to analyze this file step by step.

### Network Graphs

This folder contains network graph data in Gexf format. Gexf is a type of XML that encodes nodes, relations, and related metadata.

- [Diseasosome / diseasosome-diseases.gexf](network-graphs/diseasosome-diseases.gexf): A network graph of diseases and their connections based on the [“Human Disease Network”](https://www.pnas.org/content/104/21/8685/tab-article-info) study, which contains information about the links between the different diseases and associated genes. To simplify, we’ve removed information about the gene associations, keeping only the connections between the different diseases. The diseases are linked together if there’s at least one gene mutation that is correlated with the both diseases. Use the [network graph workflow](https://support.noduslabs.com/hc/en-us/articles/19784723159196-Gephi-Alternative-for-Network-Analysis-and-Visualization-InfraNodus) to see how to analyze this file step by step.

- [Related Artists / related-artists.gexf](network-graphs/related-artists.gexf): A network of related classic rock artists extracted from Spotify, provided by [Ifeanyi Idiaye](https://github.com/Ifeanyi55/GephiDatasets). You can see which artists are central to the field (because they are listened to with the most diverse set of artists) and which artists form clusters of interconnected communities.

- [C Elegans / celegans.gexf](network-graphs/celegans.gexf): C. elegans connectome of neurons. C. elegans is a more or less simple organism. Its adult hermaphrodite form has 302 neurons and this network shows how those neurons are connnected, which are the most central ones, and which form clusters.

- [Yeast / yeast.gexf](network-graphs/yeast.gexf): a yeast molecular interaction network that shows which proteins are more central, which form clusters, etc.

Also check out our separate archive of [network analysis datasets](https://github.com/infranodus/network-analysis-datasets)

### Knowledge Graphs

This folder contains knowledge graphs that show relations between different types of entities.

- [Knowledge Graphs / similar-sites.md](knowledge-graphs/similar-sites.md): a text file that can be uploaded to InfraNodus to analyze similar sites in SEO sphere

### Databases

This folder contains extracts from various interesting databases. For example, an extract of the research papers titles and abstracts from Arxiv up to 2025.

- [Arxiv Research Papers](databases/arxiv-graph-theory-filtered.json) contains a list of research papers on graphs extracted from [https://www.kaggle.com/datasets/Cornell-University/arxiv](https://www.kaggle.com/datasets/Cornell-University/arxiv). You can generate your own extract from the Arxiv file by using our python script [filter_graph_papers.py](databases/filter_graph_papers.py) — this script will prompt you for the categories and the keywords to look for in that file. Edit the python script if you'd like to filter a file with a different name, otherwise it will look for the file `arxiv-metadata-oai-snapshot.json` which is the default name of the file provided by Cornell university in their Kaggle dataset archive.

## License

All datasets are provided as-is and are subject to the license of the original source.

Try them out with [https://infranodus.com](https://infranodus.com).
