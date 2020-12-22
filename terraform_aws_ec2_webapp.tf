terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

data "aws_ami" "amazon_linux2_ami" {
    most_recent = true
    owners = ["amazon"]

    filter {
        name = "image-id"
        values = ["ami-04d29b6f966df1537"]
    }
}


resource "aws_security_group" "allow_webapp_traffic" {
  name        = "allow_webapp_traffic"
  description = "Allow inbound traffic"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_my_laptop"
  }
}

resource "aws_instance" "webapp" {
  ami           = data.aws_ami.amazon_linux2_ami.id
  instance_type = "t2.micro"
  vpc_security_group_ids = [aws_security_group.allow_webapp_traffic.id]
  key_name = "temp_key"

  user_data = <<-EOF
            #!/bin/bash
            sudo yum update -y
            sudo yum install httpd -y
            sudo service httpd start
            sudo chkconfig httpd on
            echo "<html><h1>Your terraform deployment worked !!!</h1></html>" | sudo tee /var/www/html/index.html
            hostname -f >> /var/www/html/index.html
            EOF

  tags = {
    Name = "myfirsttfinstance"
  }
}

output "instance_ip" {
    value = aws_instance.webapp.public_ip
}
