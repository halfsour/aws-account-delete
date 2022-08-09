from diagrams import Diagram, Edge, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.integration import Eventbridge, SQS
from diagrams.aws.management import Organizations

with Diagram():
    with Cluster("Organizations Master Account"):
        source = Eventbridge("Cron-based Event")
        gda = Lambda("getDeletableAccounts")
        mca = Lambda("moveThenCloseAccount")
        org = Organizations("AWS Organizations")
        queue = SQS("SQS Queue")

        source >> Edge(label="1. daily execution") >> gda >> queue >> Edge(label="4. trigger lambda") >> mca
        gda >> Edge(label="2. get list of accounts for closure") >> org
        #gda >> Edge(label="3. put list of accounts for closure") >> queue
        
        org << Edge(label="5. move account to 'closing' OU") << mca
        org << Edge(label="6. closeAccount") << mca