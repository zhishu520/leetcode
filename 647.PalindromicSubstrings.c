#include <string.h>
#include <stdio.h>


int extendPalindrome(char* s,int left,int right)
{
    int cnt = 0;
    int len = strlen(s);
    while(left > 0 && right < len && s[left] == s[right])
    {
        cnt++;left--;right++;
    }
    printf("cnt %d \n",cnt);
    return cnt;
}



int countSubstrings(char* s) {
    int len = strlen(s);
    int cnt = 0;
    int left,right;
    for (int i = 0; i < len; ++i) {
        cnt += extendPalindrome(s,i,i);
        cnt += extendPalindrome(s,i,i+1);
    }

    return 0;
}

int main(int argc, char *argv[])
{
    int cnt = countSubstrings("abc");
    printf("%d",cnt);
    return 0;
}
