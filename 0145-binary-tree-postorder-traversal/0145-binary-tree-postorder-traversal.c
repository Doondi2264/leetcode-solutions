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

void postHelp(struct TreeNode* r, int* a, int* rs){
    if(r==NULL)return;
    postHelp(r->left, a, rs);
    postHelp(r->right, a, rs);
    a[(*rs)++]=r->val;
    
}


int* postorderTraversal(struct TreeNode* root, int* returnSize) {
    *returnSize=0;
    int* arr = (int*)malloc(1000*sizeof(int));
    postHelp(root,arr,returnSize);
    return arr;
}



