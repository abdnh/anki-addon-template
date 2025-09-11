import { createClient } from "@connectrpc/connect";
import { createConnectTransport } from "@connectrpc/connect-web";

import { BackendService, type GetStatsResponse, type SayHelloResponse } from "./generated/backend_pb";

const transport = createConnectTransport({
    baseUrl: "/api",
    useBinaryFormat: true,
    fetch: (input, init) => {
        const headers = init?.headers ?? {};
        return fetch(input, {
            ...init,
            headers: {
                ...headers,
                "qt-widget-id": window.qtWidgetId,
            },
        });
    },
});

const client = createClient(BackendService, transport);

async function getStats(deckId: number): Promise<GetStatsResponse> {
    return client.getStats({ deckId: BigInt(deckId) });
}

async function sayHello(name: string): Promise<SayHelloResponse> {
    return client.sayHello({ name });
}

export { getStats, type GetStatsResponse, sayHello, type SayHelloResponse };
