self.KAFKA_CONFIG.update({
    # Fetch mais eficiente (puxa mais por vez)
    "fetch_max_wait_ms": 100,
    "fetch_min_bytes": 1,
    "fetch_max_bytes": 50 * 1024 * 1024,
    "max_partition_fetch_bytes": 2 * 1024 * 1024,

    # Estabilidade (evita rebalance em processamento mais lento)
    "request_timeout_ms": 60000,
    "session_timeout_ms": 30000,
    "heartbeat_interval_ms": 10000,
    "max_poll_interval_ms": 300000,
})