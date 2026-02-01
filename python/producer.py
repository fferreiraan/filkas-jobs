class KafkaProducer(Producer, CertificateManagerMixin):
    def __init__(self):
        config = {
            "client_id": KAFKA_PRODUCER_CLIENT_ID,
            **KAFKA_CONFIG,

            "linger_ms": 20,
            "batch_size": 128 * 1024,
            "compression_type": "lz4",   # se der erro, troca pra "snappy" ou remove
            "acks": 1,
            "retries": 3,

            "value_serializer": lambda x: x if isinstance(x, (bytes, bytearray)) else str(x).encode("utf-8"),
        }

        CertificateManagerMixin.__init__(self, config)
        super().__init__(**config)
