# globant-interview
This is a PoC to evaluate the technical skills of the candidate.

# Solution.
PoC uses Kafka to move records into DB based on schema.
![image](https://drive.google.com/file/d/1MKEInhm_5nHMvRkOrJu1dd6i9bsYDUV-/view?usp=sharing)

## Prerequisites.

Install following Tools on your local.

- [Conduktor](https://www.conduktor.io/)
- [anaconda](https://docs.anaconda.com/anaconda/install/index.html)

You need to set up your credentials in AWS to use AWS Glue Schema Registry to encode and decode data on the topic.

Create your enviroment to work with python

```conda env create -n globant -f src/environment.yaml```

