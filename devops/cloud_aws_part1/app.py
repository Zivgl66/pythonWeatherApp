import boto3

region='us-east-1'
ec2 = boto3.client ('ec2', region_name='region')
a = ec2.describe_instances()

#Filter all running instances
instances = ec2.instances.all(Filters=[{'Name': 'instance-state-name', 'Value': ['running']}])

#Declared list to store running instances
all_running_instances = []
specific_tag = 'Dev'
for instance in instances:
    
    #store all running instances
    all_running_instances.append(instance)
    
    #only instances with specific tag
    if instance.tag != None:
        for tags in instance.tags:
            
            #instances with tag 'Dev'
            if tags['Key'] == specific_tag:
                
                #Remove instances with specific tage from running instances
                all_running_instances.remove(instance)

# Stoping all running instances and priting message                
for specific in all_running_instances:
    print(f'Stopping EC2 instance: {specific.id}')
    specific.wait_until_stopped()
    print(f'EC2 instance: {specific.id} has been stopped.')


