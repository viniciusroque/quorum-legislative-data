# Quorum Code Questions

> 1. Discuss your strategy and decisions implementing the application. Please, consider time
complexity, effort cost, technologies used and any other variable that you understand
important on your development process.

As per design strategy & implementation, the system is split in 3 key modules:

1. Data Models: This module is designed to provide data representations of the CSV raw data and add no top it information regarding the relationship between entities. Also it user pydantic package behind the seems to enforce data checking & validation.

2. Reporting Engine: This module has 2 main features, it first has a feature to load the data from CSV and then it passes the data to different ReportProcessors (a report processor is class specialized to generate & aggregate info for a particular report; all report processors receives the same inputs).

3. Web application: This module is very minimalist, it basically calls reporting engine to get the report data and then returns an HTTP response rendering the report to users.

As per time complexity & effort cost, the code is designed to only do on one for loop (1:N) in the CSV files and with that it generates the two (legislators and bills) reports. If more reports were need to add into the system it should not increase time complexity as it basically use a concept of ReportProcessor that would process VoteResults as it gets generated and then aggregate the data only based on that. Code makes extensive use of generators making sure machine resources are used only when the data is required to be processed, for example, no need to load entire CSV files to memory before starting the processing & data aggregation.

As per technologies, python language was chosen due is the one I'm more comfortable with, and as of frameworks a) `pydantic` was used for data consistency and validations b) FastAPI for web server as it is very minimal for rendering the HTML response, say no need of all boilerplate code a Django project would generate.

Lastly Docker & Dockercompose was used in development as it simple to setup & replicate for other developers and it always allows having a local development that is similar to production servers.


> 2. How would you change your solution to account for future columns that might be
requested, such as “Bill Voted On Date” or “Co-Sponsors”?

Code is simple to be extended to support new features, for instance if we need to implement a new report "Bill Voted On Date" the code changes would consist in 1) add the new column the CSV 2) define a new field into the respective data models and then lastly 3) create a new ReportProcessor that implements ('BaseProcessor'), that would then aggregate 'VoteResult' data models per vote date.


> 3. How would you change your solution if instead of receiving CSVs of data, you were given a
list of legislators or bills that you should generate a CSV for?

For this question I'm not sure if I have the correct understanding so I'll comment my interpretation and then what changes would take to implement.

If the question is "how to change the system to allow supporting other data sources? e.g. external database, XML file, etc" - For that we would need to create a new ReportBuilder that would be specialized to read the data from the new data source and then return a list of `VoteResult` data model, with that all existing report would already work for the new data source.

If the question is "how change the system to support filtering in reporting? e.g. only return only return results of a particular legislator or stats of a particular bill" - for that we need extend the ReportProcessor to accept the new filtering_list in the constructor and then `process_vote_result` would skip any data that is not related with the filtering list.0



>4. How long did you spend working on the assignment?

I spent about 1.5 days
