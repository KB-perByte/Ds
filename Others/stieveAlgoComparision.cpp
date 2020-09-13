#include<bits/stdc++.h>

using namespace std;

#define MAXN 10000000

int lp1[MAXN+1];

void sieve1( int n )
{
  lp1[0]=lp1[1]=1;

  for(int i=2;i<=n;i+=2) lp1[i]=2;

  for(int i=3;i*i<=n;i+=2)
  {
    if(lp1[i]==0)
      for(int j=i*i;j<=n;j+=2*i)
        if(lp1[j]==0) lp1[j]=i;
  }

  for(int i=2;i<=n;i++)
    if(lp1[i]==0) lp1[i]=i;
}

int lp2[MAXN+1];
int pc = 0, pr[MAXN/10]; /* if MAXN >= 1000000 */

void sieve2( int n )
{
  lp2[0] = lp2[1] = 1;
  for( int i = 2; i <= n; ++i)
  {
    if( lp2[i] == 0 ) pr[pc++] = lp2[i] = i;
    for( int j = 0; j < pc; ++j)
    {
      int x = i * pr[j];
      if( x > n ) break;
      if( lp2[x] == 0 ) lp2[x] = pr[j];
      if( lp2[i] == pr[j] ) break;
    }
  }
}

int main()
{
  auto t1a = clock();
  sieve1( MAXN );
  auto t1b = clock();
  cout << "general sieve: " << ((double) (t1b - t1a)) / CLOCKS_PER_SEC << endl;
  auto t2a = clock();
  sieve2( MAXN );
  auto t2b = clock();
  cout << "linear sieve: " << ((double) (t2b - t2a)) / CLOCKS_PER_SEC << endl;
  for( int i = 0; i <= MAXN; ++i)
    if( lp1[i] != lp2[i] )
      cout << "Wrong lp for i = " << i << endl;
  return 0;
}
