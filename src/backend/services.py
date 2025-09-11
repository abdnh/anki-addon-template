from aqt import mw

from ..proto.backend_pb2 import GetStatsRequest, GetStatsResponse, Stats
from ..proto.services import BackendServiceBase


class BackendService(BackendServiceBase):
    @classmethod
    def get_stats(cls, request: GetStatsRequest) -> GetStatsResponse:
        graphs_response = mw.col._backend.graphs(
            search=f"did:{request.deck_id}", days=1
        )
        reviews = graphs_response.today.answer_count
        time_spent = graphs_response.today.answer_millis
        return GetStatsResponse(
            stats=Stats(
                reviews=reviews,
                time_spent=time_spent,
            )
        )
