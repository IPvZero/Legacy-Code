from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

nr = InitNornir(config_file="config.yaml")
result = nr.run(task=netmiko_send_command, command_string="show ip interface brief")
print_result(result)
