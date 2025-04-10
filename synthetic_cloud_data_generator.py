import json, random, string, time

def random_bucket_name():
    bucket_config = ['-logs','-data','-public']
    return ''.join(random.choices(string.ascii_lowercase,k = 10)) + random.choice(bucket_config)


def generate_s3_buckets(n = 5):
    s3_bucket = [
        {
            "name" : random_bucket_name(),
            "public" : random.choice([True,False]) 
        }
    ]
    return s3_bucket

def generate_security_groups(n=3):
    security_groups = []
    ip_address_choices = ["0.0.0.0/0", "192.168.1.0/24", "10.0.0.0/16"] #List of ip address available in the buckets in the cloud
    ports = [22,60,443,3306,8080]
    
    k = random.randint(1, 3)
    print(f"Sampling {k} ports")
    
    
    for i in range(n):
        ports = random.sample(ports,k = k)
        cidr = random.choice(ip_address_choices)
        security_groups.append({
            "group": f"sg-{random.randint(100,999)}",
            "open_ports": ports,
            "cidr": cidr
        })
    return security_groups


def generate_iam_users(n = 4):
    policies = ["read-only","admin","devops","*"]
    iam_users = []
    for i in range(n):
        iam_users.append({
            "username": ''.join(random.choices(string.ascii_lowercase,k = 6 )),
            "mfa_enabled": random.choice([True,False]),
            "policies": random.sample(policies,k =random.randint(1,2)),
        })
    
    return iam_users


def save_json(filename,data):
    with open(f"mock_data/{filename}","w") as f:
        json.dump(data, f, indent = 4)


def cloud_data_generator():
    #These inputs below are for sample size and can make the simualtor detect for different configurations
    no_of_s3_buckets = int(input("Enter sample size for s3_buckets: "))
    no_of_security_groups = int(input("Enter the sample size of security groups: "))
    no_of_iam_users = int(input("Enter the sample size of iam users: "))
    save_json("s3_buckets.json",generate_s3_buckets(no_of_s3_buckets))
    save_json("security_groups.json",generate_security_groups(no_of_security_groups))
    save_json("iam_users.json",generate_iam_users(no_of_iam_users))
    
    print("[+] Mock data is generated. Preparing the detector now")
    print("Loading....")
    time.sleep(4)


    