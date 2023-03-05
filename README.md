# globant-interview
This is a PoC to evaluate the technical skills of the candidate.

# Solution.
PoC uses Kafka to move records into DB based on schema.
<a href="https://drive.google.com/uc?export=view&id=1MKEInhm_5nHMvRkOrJu1dd6i9bsYDUV-"><img src="https://drive.google.com/uc?export=view&id=1MKEInhm_5nHMvRkOrJu1dd6i9bsYDUV-" style="width: 650px; max-width: 100%; height: auto" title="Click to enlarge picture" />

## Prerequisites.

Install following Tools on your local.

- [Conduktor](https://www.conduktor.io/)
- [anaconda](https://docs.anaconda.com/anaconda/install/index.html)

You need to set up your credentials in AWS to use AWS Glue Schema Registry to encode and decode data on the topic.

Create your enviroment to work with python

```conda env create -n globant -f src/environment.yaml```

