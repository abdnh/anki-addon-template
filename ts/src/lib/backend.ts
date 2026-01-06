import { createProtoClient } from "ankiutils";

import { BackendService, type GetStatsResponse, type SayHelloResponse } from "./generated/backend_pb";

export const client = createProtoClient(BackendService);

export { type GetStatsResponse, type SayHelloResponse };
