struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {
    }
};



class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {

        int down = 0,up = 0;
        ListNode* head = new ListNode(0);
        ListNode* result = head;

        while(l1 || l2)
        {
            down =  up;
            if(l1) down += l1->val;
            if(l2) down += l2->val;
            down %= 10;

            ListNode* temp = new ListNode(down);
            result->next = temp;

            if(l1) up += l1->val;
            if(l2) up += l2->val;
            up /= 10;

            result = result->next;
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
        }

        if(up != 0)
        {
            ListNode* temp = new ListNode(up);
            result->next = temp;
        }

        return head->next;
    }
};
