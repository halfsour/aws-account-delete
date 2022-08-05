## AWS Account Closer

This template will create a Cloudformation stack that contains the resources necessary to check a specific OU in an AWS Organization for accounts that are beyond the maximum age that you set.  Any accounts found that match that criteria are moved to a different OU, tagged as an account to be closed and then closed.  This marks the AWS account as "Suspended" for 90 days.  During that time, the account cannot be access and billing will stop.

#### Important:
AWS restricts how frequently the CloseAccount API can be used within a 30 day period to 10% of the accounts in the AWS Organization.  As such, if you run in to this throttle condition, the account will still remain in the closing OU but it will still be open and therefore chanrges will continue to accrue any billable resources.  You can mitigate this by closing the account manually if you see that the function is failing due to this condition.

### Prerequisites:
- AWS Organizations configured with at least 3 Organization Units (OU):
    - An OU for actively used accounts
    - An OU for closing accounts
    - An OU for crititcal accounts that should never be deleted with this automation 

### Deployment:
This is a single-stack clpudformation temolate can it can be deployed via the CLI or AWS Console

Exampl via the CLI:
```bash
aws cloudformation deploy --template-file ./AutoDeleteAccounts.yaml --stack-name autoCloseAccounts --parameter-overrides age=30 activeOuId=ou-1234-abcdefgh closingOuId=ou-wxyz-a1b2c3d4
```
### See Also:
[Why did I receive a bill after I closed my AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/closed-account-bill/)  
[How can I reactivate my suspended AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/reactivate-suspended-account/)  
[Best Practices for Organizational Units with AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-for-organizational-units-with-aws-organizations/)  
[How do I close my AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/close-aws-account/)  