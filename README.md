Data product from [NEON Zooplankton collection](https://data.neonscience.org/data-products/DP1.20219.001) (DP1.20219.001)

## Directories
- ~~DaphniaData directory includes main.py file that filters zooplankton collection data to only consider Daphnia and then generate figures from the processed .csv files.~~
  
- The `main.py` file has been moved to the root directory. The `DaphniaData` directory has been removed.
- The `main.py` file has been updated to include the following:
  - The `main.py` file now includes a function to filter the zooplankton collection data to only consider Daphnia.
  - The `main.py` file now includes a function to generate figures from the processed .csv files.

- The `data` directory stores the source and processed csv files for this project. If you want to run the `main.py` file, you will need to download the source csv file from the NEON data portal and place it in the `data` directory. The processed csv files will be saved to the `data` directory.

- The `figures` directory includes subdirectories with graphs of the daphnia count in each site, the count per year in each site and the size per year in each site.
  
## Additional Information About Data

**Table 1.** Neon Aquatic Sites sampled for Zooplankton collection (modified from NEON.DOC.00152vB)
| Domain Number	| Site ID |	Site Name	| Site Class | Domain Name | Type	| State |
| ------------- | ------- | --------- | ---------- | ----------- | ---- | ----- |
| 03 | BARC	| Barco Lake | Lake | Southeast | Core |	FL |
| 03 | SUGG	| Suggs Lake | Lake |	Southeast |	Core | FL |
| 05 | CRAM	| Carmpton Lake	| Lake | Great Lakes | Core	| WI |
| 05 | LIRO | Little Rock Lake | Lake | Great Lakes | Core | WI |
| 09 | PRPO | Prairie Pothole | Lake | Northern Plains | Core | ND |
| 09 | PRLA | Prairie Lake | Lake | Northern Plains | Gradient | ND |
| 18 | TOOK | Toolik Lake | Lake | Tundra | Gradient | AK |

*Note: The difference between core and gradient sites: Core aquatic sites are located in areas that are not significantly influenced by built structures, e.g., bridges, or human activities that may impact water quality, such as urbanization, agriculture, or wastewater effluent. Gradient aquatic sites are located in order to capture environmental gradients.

