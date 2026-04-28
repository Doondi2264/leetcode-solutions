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


void inorderHelp(struct TreeNode* root, int* result, int* returnSize){
    if(root==NULL)return;
    inorderHelp(root->left, result, returnSize);
    result[(*returnSize)++]=root->val;
    inorderHelp(root->right, result, returnSize);
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize=0;
    int* result = (int*)malloc(1000*sizeof(int));
    inorderHelp(root,result,returnSize);
    return result;
}
