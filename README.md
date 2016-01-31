#donald trump magic 8 ball alexa app
##it's gonna be YUGE

how to use:

0. get yourself in a python 2.7 environment
1. `pip install -r requirements-dev.txt`
2. `cp config.yml.example config.yml`
3. update your config.yml. pay special attention to IAM policy, IAM role, and profile.
4. `kappa config.yml create`
5. add Alexa Skills Kit as an event source on the lambda function in the AWS console. there doesn't seem to be a way to do this yet through any standard tooling. I'll try to circle back on this later -- it likely requires a PR into https://github.com/garnaat/kappa
6. fill out the forms to create an alexa application (https://developer.amazon.com/edw/home.html) and connect your lambda function to it. you can get the function's ARN from `kappa config.yml status`. you'll also need to paste in the intent_schema and sample_utterances.
