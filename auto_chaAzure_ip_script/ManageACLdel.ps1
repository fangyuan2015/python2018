<# 	This script is for Automatic VM Endpoint ACL Management.
	Please edit Files (addACL.csv and removeACL.csv) first. Keep them in the same PATH as this script.
	Confirm your current working path and run this script.
	
	Files: 	addACL.csv {ServiceName, VMName, EndpointName, Order, Action, RemoteSubnet, Description}
			removeACL.csv {ServiceName, VMName, EndpointName, ruleID}
	Param:	-operation Add/Remove (case insensitive)
	Author: Azure Mooncake Support Team(Net pod), Microsoft. 
#>

	#(2) Remove Endpoints from .scv {ServiceName, VMName, EndpointName, ruleID}
	# 	 Please list ACL in descend order of ruleID for each Endpoint. RuleID is the index of your ACL, start from 0.
Import-Csv C:\20170316-script-ACLManagement\removeACL.csv | foreach {
	$vm = Get-AzureVM -ServiceName $_.ServiceName -Name $_.VMName;
	$acl = $vm | Get-AzureAclConfig -EndpointName $_.EndpointName;
	Set-AzureAclConfig -RemoveRule -RuleId $_.ruleID -ACL $acl;
	$vm | Set-AzureEndpoint -ACL $acl -Name $_.EndpointName | Update-AzureVM;
}


<# You can check current endpoints with the following two ways.
		Portal: Virtual Machine - Endpoints)
		Powershell command: "$vm | Get-AzureAclConfig -EndpointName yourEndpoint"
#>