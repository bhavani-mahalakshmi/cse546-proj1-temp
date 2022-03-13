import boto3

ec2_client = boto3.client('ec2',region_name='us-east-1')

AMI_ID = "ami-0c54829ef6df8e025"

def create_instance():
    print("Creating new instance")
    instances = ec2_client.run_instances(
        ImageId=AMI_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="AWS-EC2-SRIK"
    )
    print("Done creating instance")
    print("Instance id:", instances["Instances"][0]["InstanceId"])

def bulk_create_instances(num):
    print("Starting bulk create of", num, "instances")
    for _ in range(num):   
        create_instance() 

def start_instance(instance_id):
    print('Starting instance with ID:',instance_id)
    response = ec2_client.start_instances(InstanceIds=[instance_id], DryRun=False)
    print(response)
   
def bulk_start_instances(instance_ids):
    print("Starting these instances", instance_ids)
    for i in instance_ids:
        start_instance(i)

def stop_instance(instance_id):
    print("Stopping instance:", instance_id)
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)

def bulk_stop_instances(instance_ids):
    print("Stopping these instances", instance_ids)
    for i in instance_ids:
        stop_instance(i)

def get_running_instances():
    instance_list = []
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running", "pending"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_list.append(instance_id)
    print("Here are your instances:", instance_list)
    return instance_list

def get_stopped_instances():
    instance_list = []
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["stopped"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_list.append(instance_id)
    print("Here are your instances:", instance_list)
    return instance_list

def get_all_instances():
    instance_list = []
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running", "stopped"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_list.append(instance_id)
    print("Here are your instances:", instance_list)
    return instance_list

def get_stopped_instances():
    instance_list = []
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["stopped"],
        }
    ]).get("Reservations")

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_list.append(instance_id)
    print("Here are your instances:", instance_list)
    return instance_list    