import boto3
from aws_schema_registry import SchemaRegistryClient
from aws_schema_registry.avro import AvroSchema
from aws_schema_registry.adapter.kafka import KafkaSerializer
from kafka import KafkaProducer
from config.get_schema import GetSchemas


"""
Produce message to insert in kafka topic, the name and schema are related to source name
Arguments:
    row: Series within source definition
    source: source name 
Returns:
   Record metadata to locate the record in the topic 
"""
def producer_msg(row, source):
    session = boto3.Session(aws_access_key_id='AKIA3CAXUPMKKDB37HMQ', aws_secret_access_key='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')

    glue_client = session.client('glue', region_name='us-east-1')
    
    # Create the schema registry client
    client = SchemaRegistryClient(glue_client=glue_client, registry_name='my-registry')
    
    # Create the serializer
    serializer = KafkaSerializer(client)
    
    # Create the producer
    producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'], value_serializer=serializer)
    
    # Our producer needs a schema to send along with the data
    # In this example we're using Avro
    
    with open(f'data/schema_registry/{source}.avsc','r') as file:
        schema = AvroSchema(file.read())
    
    func_schema= getattr(GetSchemas, f'json_{source}')

    data= func_schema(GetSchemas, row)

    record_metadata= producer.send(source, value=(data, schema)).get(timeout=10)
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)