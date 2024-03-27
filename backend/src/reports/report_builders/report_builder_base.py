import abc
from typing import Any, Iterable

from data_models.vote_results import VoteResult
from reports.report_processors.report_processors_interface import (
    ReportProcessorInterface,
)


class ReportBuilderBase:

    @abc.abstractmethod
    def _fetch_vote_result(self) -> Iterable[VoteResult]:
        raise NotImplementedError("You must implement this method")

    def build_report(self, reports_processors: list[ReportProcessorInterface]):
        for vote_result in self._fetch_vote_result():
            for report_processor in reports_processors:
                report_processor.process_vote_result(vote_result)


# class ReportBuilderDB(ReportBuilderBase):

#     def _fetch_vote_result(self) -> Iterable[VoteResult]:
#         for data in self._fetch_vote_result_from_db():
#             yield VoteResult(data)
