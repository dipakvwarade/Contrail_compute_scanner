# Contrail Compute Scanner

CCS use a simple custom fact written in python to fetch the configuration and operational states from computes in JSON format.
Since the script is written in python its very easy to expand to cover other use cases.



# How to use ?
```
git clone git@github.com:dipakvwarade/Contrail_compute_scanner.git
cd Contrail_compute_scanner
[stack@rhosp]$ ANSIBLE_TIMEOUT=5000;ansible-playbook -i inventory cn_compute_scanner.yml

```

# Whats covered for now?
- Mainly Contrail related configuration and operational states like routing table, vrfs, mpls, vxlan etc
- I'll be adding a support to cover SRIOV and DPDK config and operation status

# Improvements planned
- Have an option to dump each command seperately
- Dynamic inventories to cover newly deployed nodes
- How to improve speed?
- SRIOV node scanning - cover all aspect of sriov compute
- DPDK node scanning - cover all aspect of dpdk compute
- Cover Fabric nodes - vlan tagging, MTU etc



