# blockballot
Bitcamp 2018 Hack to create a blockchain voting system.

Fork of ARK to allow an election. Delegate election results are stored forever in the blockchain, preventing fraudulent or faked voting. Since the infrastructure already allows voting for delegates, I am creating a system to allow humans to create an ARK wallet associated with an ID. They visit the website and fill out a google form (could later be updated to a SQL database in order to not rely on google).  Then, the election agency(genesis wallet owner) can distribute the exact amount of coin necessary to submit a vote. The ARK-Python api is used for the election administrator to be able to make a large number of 1 MBT transactions to all eligible voters.  I used the ARK.io guides to setup a bridgechain node, with some unique configuration options in the arkballotinstall.sh file. 

The main change between use cases is the reward per block for maintaining a node. In a large system, like a government, this should be small or zero and delegates (new office holders) should instead be paid their government salary as incentive to maintain a node. Alternatively, a public institution could do the labor of maintaining the node so that officials do not have to be fully technically literate. In a smaller one, delegates and officials are more accountable to the community are a part of and so the solution to a reward for maintaining the blockchain is more nebulous. This is a factor for the group in question to decide. 

The illustrative case will be a UMD student group. For this group, members have to pay dues. They will pay the election administrator (genesis wallet owner) dues for the year to obtain a coin to vote and the administrator will be responsible for depositing these USD into the group treasury. As a reward for maintaining the nodes, the delegates for this group will not have to pay dues for the year. 

The implemented solution does not rely on a dues paying organization. However, an organization that does pay dues could run the Names/Addresses file against their database of dues paying members.
