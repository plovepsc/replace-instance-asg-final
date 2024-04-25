resource "aws_autoscaling_group" "example" {
  name = "production-testasg"
  desired_capacity     = "${var.desire_capasity}"
  max_size             = 2
  min_size             = 1
  health_check_type    = "ELB"
  health_check_grace_period = 300


  launch_template {
    id = "lt-0c0fea8f7d8796c99"
    version = "$Latest"
  }

  vpc_zone_identifier = ["subnet-00fa0324cc16542a8, subnet-00f2b33dd30fcf6eb"]  # Specify your subnet IDs
  termination_policies = [
    "OldestInstance"
  ]
 

  tag {
    key                 = "Name"
    value               = "your-instance-name-you-show"
    propagate_at_launch = true
  }
}
