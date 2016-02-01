#donald trump magic 8 ball alexa app

This is a completely functional Amazon Echo Alexa app. If you have one and are willing to install this on your device, let me know what you think. Pull requests welcome, particularly if there are new quotes to add. :)


##it's gonna be YUGE

<img src="/logo.jpg" height="300" width="300">

To use on your Amazon Echo:

1. enable the "Ask Trump" skill
1. Ask Trump something


To develop your own:

1. get yourself into a python2.7 environment because AWS Lambda doesn't support python3 yet
1. `pip install -r requirements-dev.txt`
1. `cp config.yml.example config.yml`
1. update your config.yml. pay special attention to IAM policy, IAM role, and profile.
1. `kappa config.yml create` will create your lambda function in your AWS account
1. add Alexa Skills Kit as an event source on the lambda function in the AWS console. There doesn't seem to be a way to do this yet through any standard tooling. I'll try to circle back on this later, because it likely requires a PR into https://github.com/garnaat/kappa
1. fill out the forms to create an Alexa application (https://developer.amazon.com/edw/home.html) and connect your lambda function to it. ou can get the function's ARN from `kappa config.yml status`. you'll also need to paste in the intent_schema and sample_utterances from the files in the root directory of the repo.

