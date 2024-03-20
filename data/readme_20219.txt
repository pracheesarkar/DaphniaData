###################################
########### Disclaimer ############
This is the most recent readme publication based on all site-date combinations used during stackByTable.
Information specific to the query, including sites and dates, has been removed. The remaining content reflects general metadata for the data product.
##################################

This data package was produced by and downloaded from the National Ecological Observatory Network (NEON). NEON is funded by the National Science Foundation (Awards 0653461, 0752017, 1029808, 1138160, 1246537, 1638695, 1638696, 1724433) and managed cooperatively by Battelle. These data are provided under the terms of the NEON data policy at https://www.neonscience.org/data-policy.
DATA PRODUCT INFORMATION
------------------------
ID: NEON.DOM.SITE.DP1.20219.001
Name: Zooplankton collection
Description: Collection of zooplankton from water column samples in lakes
NEON Science Team Supplier: Aquatic Observation System
Abstract: This data product contains the quality-controlled, native sampling resolution data and metadata from NEON's aquatic zooplankton collection protocol, as well as associated taxonomic, morphometric, and count analyses data provided by a contracted lab. Field samples are collected in the water column of lakes using the most appropriate sampler (vertical tow net or Schindler trap) for the depth of water, preserved in ethanol in the field, and shipped to a contracting lab for analysis. For additional details, see the user guide, protocols, science design, and lab SOPs listed in the Documentation section in this data product's details webpage.
Latency:
The expected time from data and/or sample collection in the field to data publication is as follows, for each of the data tables (in days) in the downloaded data package. See the Data Product User Guide for more information.
zoo_fieldData:  30
zoo_perSample:  210
zoo_taxonomyProcessed:  210
zoo_taxonomyRaw:  210
zoo_perVial:  210
zoo_identificationHistory: 7
Brief Design Description: Zooplankton samples are collected three times per year at lake sites during aquatic biology bout windows, roughly in spring, summer, and fall. Samples are collected using either a tow net (water deeper than 4 m) or a Schindler-Patalas trap (water shallower than 4 m) depending on the depth at the sampling location. Samples are collected near the NEON profiling buoy as well as two littoral sensor sets. Samples are preserved in ethanol in the field and shipped to a taxonomy lab for sorting and identification, including count of each taxon, summary length and width measurements for each taxon per sample (to nearest mm) and identification to lowest practical taxon (genus or species).
Brief Study Area Description: These data are collected at all NEON aquatic lake sites.
Sensor(s): 
Keywords: water column, biodiversity, zooplankton, archived samples, ZOO, species composition, lake, rotifers, crustaceans, community composition, diversity, population, aquatic, pelagic, taxonomy, abundance, material samples
Domain: D03
DATA PACKAGE CONTENTS
---------------------
This folder contains the following documentation files:
This data product contains up to 6 data tables:
- Term descriptions, data types, and units: NEON.D03.BARC.DP1.20219.001.variables.20231226T225809Z.csv
zoo_taxonomyProcessed - Aquatic zooplankton identifications by expert taxonomists - desynonimized
zoo_fieldData - Aquatic zooplankton field data
zoo_taxonomyRaw - Aquatic zooplankton identifications by expert taxonomists - raw
zoo_perVial - Aquatic zooplankton identified archive data
zoo_perSample - Zooplankton subsampling data and QC metrics per sample
zoo_identificationHistory - Aquatic zooplankton identification history for records where identifications have changed
If data are unavailable for the particular sites and dates queried, some tables may be absent.
Basic download package definition: The basic data package includes all field measurements and presents higher taxonomy information according to NEON and reassigns synonymies with the current valid name.
Expanded download package definition: The expanded data package includes an additional file that includes the taxonomic nomenclature as received from the external taxonomist.
FILE NAMING CONVENTIONS
-----------------------
NEON data files are named using a series of component abbreviations separated by periods. File naming conventions for NEON data files differ between NEON science teams. A file will have the same name whether it is accessed via NEON's data portal or API. Please visit https://www.neonscience.org/data-formats-conventions for a full description of the naming conventions.
ISSUE LOG
----------
This log provides a list of issues that were identified during data collection or processing, prior to publication of this data package. For a more recent log, please visit this data product's detail page at https://data.neonscience.org/data-products/DP1.20219.001.
Issue Date: 2023-12-22
Issue: Identification history: updates to taxonomic determinations were not previously tracked.
       Date Range: 2012-01-01 to 2023-01-01
       Location(s) Affected: All
Resolution Date: 2024-01-01
Resolution: In provisional data, RELEASE-2024, and all subsequent releases, if taxonomic determinations are updated for any records, past determinations are archived in the `zoo_identificationHistory` table, where the archived determinations are linked to current records using identificationHistoryID.
Issue Date: 2023-05-09
Issue: D01 state-level taxa obfuscation: Prior to the 2024 data release, publication of species identifications were obfuscated to a higher taxonomic rank when the taxon was found to be listed as threatened, endangered, or sensitive by any state within the domain. Obfuscating state-listed taxa across an entire domain has created challenges for data users studying biodiversity.
       Date Range: 2012-01-01 to 2023-04-25
       Location(s) Affected: D01
Resolution Date: 2023-12-31
Resolution: To reduce the number of records in which taxonomic identifications are obfuscated in D01, the state-level obfuscation routine has been applied to data using site-level granularity as of 25 April 2023. Previously published data have been reprocessed using the more precise obfuscation routine for the 2024 data release and onward. Federally listed threatened and endangered or sensitive species remain obfuscated at all sites.
Issue Date: 2022-09-15
Issue: Toolik Field Station required a quarantine period prior to starting work in the 2020, 2021, and 2022 field seasons to protect all personnel during the COVID-19 pandemic. This complicated NEON field scheduling logistics, which typically involves repeated travel across the state on short time frames. Consequently, NEON reduced staff traveling to Toolik and was thus unable to complete all planned sampling efforts. Missed data collection events are indicated in data records via the samplingImpractical field.
       Date Range: 2020-03-23 to 2022-12-31
       Location(s) Affected: TOOK
Resolution Date: 2022-10-31
Resolution: The quarantine policy at Toolik Field Station ended after the 2022 field season.
Issue Date: 2022-11-15
Issue: Incorrect namedlocation: The incorrect named location was published for littoral surface water, biological, and sediment sampling at Toolik Lake.
       Date Range: 2017-01-01 to 2022-10-20
       Location(s) Affected: TOOK
Resolution Date: 2022-10-20
Resolution: Data collected in this data product through the resolution date with **namedLocation** equal to TOOK.AOS.littoral1 was edited to equal TOOK.AOS.littoral3.
Issue Date: 2021-12-01
Issue: Miscalculated volumes: Data in the fields "zooSubsampleVolume" and "adjCountPerBottle" are incorrect due to a miscalculation in subsample volume at the external lab. Only affects data from the Rhithron lab.
       Date Range: 2019-04-24 to 2021-07-15
       Location(s) Affected: BARC, CRAM, LIRO, PRLA, PRPO, SUGG, TOOK
Resolution Date: 2022-01-01
Resolution: Calculations have been fixed and data edited. All data should be correct as of Release 2022
Issue Date: 2021-01-06
Issue: Safety measures to protect personnel during the COVID-19 pandemic resulted in reduced or canceled sampling activities for extended periods at NEON sites. Data availability may be reduced during this time.
       Date Range: 2020-03-23 to 2021-12-31
       Location(s) Affected: All
Resolution Date: 2021-12-31
Resolution: The primary impact of the pandemic on observational data was reduced data collection. Training procedures and data quality reviews were maintained throughout the pandemic, although some previously in-person training was conducted virtually.  Scheduled measurements and sampling that were not carried out due to COVID-19 or any other causes are indicated in data records via the samplingImpractical data field.
Issue Date: 2021-12-09
Issue: State-level taxa obfuscation: Prior to the 2022 data release, publication of species identifications were obfuscated to a higher taxonomic rank when the taxon was found to be listed as threatened, endangered, or sensitive at the state level where the observation was recorded. Obfuscating state-listed taxa has created challenges for data users studying biodiversity.
       Date Range: 2012-01-01 to 2021-12-31
       Location(s) Affected: All
Resolution Date: 2021-12-31
Resolution: The state-level obfuscation routine was removed from the data publication process at all locations excluding sites located in D01 and D20. Data have been reprocessed to remove the obfuscation of state-listed taxa. Federally listed threatened and endangered or sensitive species remain obfuscated at all sites and sensitive species remain redacted at National Park sites.
Issue Date: 2020-10-20
Issue: Inlet Outlet Names: Near-shore sampling locations in all lake sites were named 'inlet' and 'outlet' even if the site was a seepage lake that has no single inlet or outlet.
       Date Range: 2014-07-01 to 2020-12-31
       Location(s) Affected: BARC, CRAM, LIRO, PRLA, PRPO, SUGG, TOOK
Resolution Date: 2020-12-31
Resolution: Near-shore collection sites at seepage lakes are now called 'littoral1' and 'littoral2', where 'littoral1' corresponds to previous site name 'inlet' and 'littoral2' corresponds to previous site name 'outlet'.
Issue Date: 2020-10-20
Issue: No Standard Taxonomic Effort: External taxonomy labs not using standard taxonomic effort
       Date Range: 2014-07-01 to 2018-10-01
       Location(s) Affected: BARC, SUGG, CRAM, LIRO, PRPO, PRLA, TOOK
Resolution Date: 2018-10-01
Resolution: External labs began using standardized taxonomic effort for identification targets, references, and measurement .
ADDITIONAL INFORMATION
----------------------
Protection of species of concern: At most sites, taxonomic IDs of species of concern have been 'fuzzed', i.e., reported at a higher taxonomic rank than the raw data, to avoid publishing locations of sensitive species. For a few sites with stricter regulations (e.g., Great Smoky Mountains National Park (GRSM)), records for species of concern are not published. 
Queries for this data product will return all data for `zoo_fieldData`, `zoo_perSample`, and `zoo_taxonomyProcessed` during the date range specified. If sampling is not impractical, each record for in `zoo_fieldData` has 1 record in `zoo_perSample` and may have multiple corresponding records in `zoo_taxonomyRaw` and `zoo_taxonomyProcessed`, one record for each scientificName per sampleID. A record from `zoo_fieldData` may have multiple or no records in `zoo_perVial`, as that table represents individuals removed from the final archived sample and placed in the external lab's in-house reference collection, records in this table are opportunistic.  The expanded package also returns raw taxonomic data from the external taxonomist in `inv_taxonomyRaw` and information on the contents of the vial sent to the archive facility in `inv_perVial`. Duplicates may exist where protocol and/or data entry aberrations have occurred; users should check data carefully for anomalies before analyzing data. Taxonomic IDs of species of concern have been 'fuzzed'; see data package readme files for more information. If taxonomic determinations have been updated for any records in the tables `zoo_taxonomyProcessed` or `zoo_taxonomyRaw`, past determinations are archived in the `zoo_identificationHistory` table, where the archived determinations are linked to current records using identificationHistoryID.
NEON DATA POLICY AND CITATION GUIDELINES
----------------------------------------
A citation statement is available in this data product's detail page at https://data.neonscience.org/data-products/DP1.20219.001. Please visit https://www.neonscience.org/data-policy for more information about NEON's data policy and citation guidelines.
DATA QUALITY AND VERSIONING
---------------------------
NEON data are initially published with a status of Provisional, in which updates to data and/or processing algorithms will occur on an as-needed basis, and query reproducibility cannot be guaranteed. Once data are published as part of a Data Release, they are no longer provisional, and are associated with a stable DOI.
To learn more about provisional versus released data, please visit https://www.neonscience.org/data-revisions-releases.
