/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

void prehelp(struct TreeNode* r,int* a,int*i);

int* preorderTraversal(struct TreeNode* root, int* returnSize) {
    int*r=(int*)malloc(100 * sizeof(int));
    *returnSize=0;
    prehelp(root,r,returnSize);
    return r;
}
void prehelp(struct TreeNode* r,int* a,int*i){
    if (r==NULL)return ;
    a[(*i)++]=r->val;
    prehelp(r->left,a,i);
    prehelp(r->right,a,i);
}