kafka-console-consumer --bootstrap-server broker-1:29092 --topic wordcount-output-topic --property print.key=true --from-beginning  --consumer-property group.id=output-consumer --property "value.deserializer=org.apache.kafka.common.serialization.LongDeserializer"