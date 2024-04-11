#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define ms(arr,b) memset(arr,b,sizeof(arr))
#define mp make_pair
#define F first
#define S second
#define all(v) v.begin(),v.end()
#define ll long long
#define ld long double

int gcd(int a,int b,int& x,int& y){
  if(b==0){
    x = 1;
    y = 0;
    return a;
  }
  int x1, y1;
  int d = gcd(b,a%b,x1,y1);
  x = y1;
  y = x1-y1*(a/b);
  return d;
}
void solve(){
  
}


int main(){
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t=1;
  //cin>>t;
  while(t--){
    solve();
    cout<<'\n';
  }
}

