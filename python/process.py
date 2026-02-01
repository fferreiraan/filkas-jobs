try:
    ping_log.info(f"Mensagem recebida offset={message.offset}")

    res, err = fping(**validate_data(message.value))

    processed = False  # só comita se processou (produziu) ou descartou de propósito

    if res:
        linhas_filtradas = (
            linha for linha in res.splitlines()
            if "xmt/rcv/%loss = 1/0/100%" not in linha
        )
        res_filtrado = "\n".join(linhas_filtradas).strip()

        if res_filtrado:
            send_future = producer.send(TOPIC_NAME_PRODUCER, res_filtrado)
            send_future.get(timeout=10)  # garante ACK do Kafka de saída
            ping_log.info("Mensagem enviada com sucesso.")
        else:
            # decidiu descartar (tudo 100% loss). IMPORTANTE: considera processado.
            ping_log.info("Descartado (tudo 100% loss).")

        processed = True
    else:
        # fping não retornou res -> NÃO considera processado
        ping_log.warning(f"fping sem saída. stderr={err}")

    # Commit só quando processou (ou descartou conscientemente)
    if processed:
        count += 1
        if count % 100 == 0:
            consumer.commit()

except Exception as e:
    ping_log.error(f"Erro ao processar offset={getattr(message,'offset',None)}: {e}")
    continue
