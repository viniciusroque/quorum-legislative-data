from reports.report_builders.report_builder_csv import ReportBuilderCSV, ReportError
from reports.report_processors.bills_report_processor import BillsReportProcessor
from reports.report_processors.legislators_report_processor import (
    LegislatorsReportProcessor,
)

LEGISLATOR_CSV_PATH = "/usr/app/backend/data/legislators_(2).csv"
BILLS_CSV_PATH = "/usr/app/backend/data/bills_(2).csv"
VOTES_CSV_PATH = "/usr/app/backend/data/votes_(2).csv"
VOTE_RESULTS_CSV_PATH = "/usr/app/backend/data/vote_results_(2).csv"


def get_reports() -> (
    tuple[
        LegislatorsReportProcessor, BillsReportProcessor, dict[str, list[ReportError]]
    ]
):
    report_builder = ReportBuilderCSV(
        legislator_csv_path=LEGISLATOR_CSV_PATH,
        bill_csv_path=BILLS_CSV_PATH,
        vote_csv_path=VOTES_CSV_PATH,
        vote_result_csv_path=VOTE_RESULTS_CSV_PATH,
    )

    legislator_report = LegislatorsReportProcessor()
    bills_report = BillsReportProcessor()

    report_builder.build_report([legislator_report, bills_report])

    return legislator_report, bills_report, report_builder.get_errors()
