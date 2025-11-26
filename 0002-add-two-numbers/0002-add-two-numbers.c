/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* createnode(int n);

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* t=createnode(0);
    struct ListNode* c = t;
    int carry = 0;
    while(l1 || l2 || carry){
        int a = (l1)?l1->val:0;
        int b = (l2)?l2->val:0;
        int sum = a+b+carry;
        carry = sum/10;
        c->next=createnode(sum%10);
        c=c->next;
        if(l1)l1=l1->next;
        if(l2)l2=l2->next;

    }
    return t->next;
}

struct ListNode* createnode(int n){
    struct ListNode* nn = (struct ListNode*)malloc(sizeof(struct ListNode));
    nn->val=n;
    nn->next=NULL;
    return nn;
}