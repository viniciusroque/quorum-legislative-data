from collections import defaultdict
from typing import Any, Iterable

from data_models.bills import Bill, BillMapping
from data_models.legislators import Legislator, LegislatorMapping
from data_models.mapping_interface import MappingInterface
from data_models.vote_results import VoteResult
from data_models.votes import Vote, VoteMapping
from lib.csv_parser import parse_csv
from pydantic import ValidationError, dataclasses
from reports.bills_report import BillsReport
from reports.legislators_report import LegislatorsReport


@dataclasses.dataclass
class ReportError:
    line_number: int
    error: str
    raw_data: dict[str, Any]


def create_record[
    BaseDataModel: type[Legislator | Bill | Vote | VoteResult],
](
    record: BaseDataModel,
    mapping: MappingInterface,
    row: dict[str, Any],
    line_number: int,
) -> (tuple[BaseDataModel, None] | tuple[None, ReportError]):

    if mapping.get_by_id(row.get("id", -1)):
        return None, ReportError(
            line_number=line_number,
            error="Duplicated record.",
            raw_data=row,
        )
    try:
        data_model = record(**row)
    except ValidationError as e:
        return None, ReportError(
            line_number=line_number, error=str(e.errors()[0]["msg"]), raw_data=row
        )

    return data_model, None


class ReportBuilder:
    _legislators: LegislatorMapping
    _legislator_csv_path: str
    _bills: BillMapping
    _bill_csv_path: str
    _votes: VoteMapping
    _vote_csv_path: str
    _vote_result_csv_path: str
    _errors: dict[str, list[ReportError]] = defaultdict(list)

    def __init__(
        self,
        legislator_csv_path: str,
        bill_csv_path,
        vote_csv_path,
        vote_result_csv_path,
    ) -> None:
        self._legislators = LegislatorMapping()
        self._bills = BillMapping()
        self._votes = VoteMapping()
        self._legislator_csv_path = legislator_csv_path
        self._bill_csv_path = bill_csv_path
        self._vote_csv_path = vote_csv_path
        self._vote_result_csv_path = vote_result_csv_path
        self._errors = defaultdict(list)

    def _load_legislator(self):
        for line_number, row in parse_csv(self._legislator_csv_path):
            legislator, error = create_record(
                Legislator, self._legislators, row, line_number
            )
            if error:
                self._errors[self._legislator_csv_path].append(error)
                continue

            assert isinstance(legislator, Legislator)
            self._legislators.add(legislator)

    def _load_bill(self):
        for line_number, row in parse_csv(self._bill_csv_path):
            sponsor_id = row["sponsor_id"]
            row["primary_sponsor"] = self._legislators.get_by_id(sponsor_id)
            bill, error = create_record(Bill, self._bills, row, line_number)
            if error:
                self._errors[self._bill_csv_path].append(error)
                continue

            assert isinstance(bill, Bill)
            self._bills.add(bill)

    def _load_vote(self):
        for line_number, row in parse_csv(self._vote_csv_path):
            row["bill"] = self._bills.get_by_id(row["bill_id"])
            vote, error = create_record(Vote, self._votes, row, line_number)
            if error:
                self._errors[self._vote_csv_path].append(error)
                continue

            assert isinstance(vote, Vote)
            self._votes.add(vote)

    def _fetch_vote_result(self) -> Iterable[VoteResult]:
        for line_number, row in parse_csv(self._vote_result_csv_path):
            row["legislator"] = self._legislators.get_by_id(row["legislator_id"])
            row["vote"] = self._votes.get_by_id(row["vote_id"])

            vote_result, error = create_record(
                VoteResult, self._votes, row, line_number
            )
            if error:
                self._errors[self._vote_result_csv_path].append(error)
                continue

            assert isinstance(vote_result, VoteResult)
            yield vote_result

    def build_report(self, reports_processors: list[LegislatorsReport | BillsReport]):
        self._load_legislator()
        self._load_bill()
        self._load_vote()
        for vote_result in self._fetch_vote_result():
            for report_processor in reports_processors:
                report_processor.process_vote_result(vote_result)

    def get_errors(self) -> dict[str, list[ReportError]]:
        return self._errors
