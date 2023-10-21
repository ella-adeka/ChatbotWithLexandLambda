import boto3

print('Loading chat...')
lex = boto3('lex', region_name='eu-west-2')

def lambda_function(event, context):
    
    try:
      print(event)
    except Exception as e:
      print('An exception occurred')
 