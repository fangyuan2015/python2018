<# 	This script is for Automatic VM Endpoint ACL Management.
	Please edit Files (addACL.csv and removeACL.csv) first. Keep them in the same PATH as this script.
	Confirm your current working path and run this script.
	
	Files: 	addACL.csv {ServiceName, VMName, EndpointName, Order, Action, RemoteSubnet, Description}
			removeACL.csv {ServiceName, VMName, EndpointName, ruleID}
	Param:	-operation Add/Remove (case insensitive)
	Author: Azure Mooncake Support Team(Net pod), Microsoft. 
#>


Import-Csv C:\20170316-script-ACLManagement\addACL.csv | foreach {
	$vm = Get-AzureVM -ServiceName $_.ServiceName -Name $_.VMName;
	$acl = $vm | Get-AzureAclConfig -EndpointName $_.endpointName;
	Set-AzureAclConfig -AddRule -ACL $acl -Order $_.Order -action $_.Action -RemoteSubnet $_.RemoteSubnet -Description $_.Description;
	$vm | Set-AzureEndpoint -ACL $acl -Name $_.EndpointName | Update-AzureVM;
	}