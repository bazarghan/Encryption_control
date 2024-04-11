#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define ms(arr,b) memset(arr,b,sizeof(arr))
#define mp make_pair
#define F first
#define S second
#define all(v) v.begin(),v.end()
#define ll uint64_t
#define ld long double


const int mymod = 1e9+7;

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


int factorial(int n){
  ll res = 1;
  for(int i=1;i<=n;i++){
    res = (res*i)%mymod;
  }
  int ans = res;
  return ans;
}

ll mul(ll a,ll b,ll mod){
  if(b<=1) return b?a:0;
  ll ans = mul(a,b>>1,mod);
  ans = (ans+ans)%mod;
  if(b&1) ans = (ans+a)%mod;
  return ans;
}


ll pow(ll a,ll n,ll mod){
  if(n==0) return 1ULL;
  ll mya = pow(a,n/2,mod);
  ll d = mul(mya,mya,mod);
  if(n%2==1) d = mul(d,a,mod);
  return d;
}


ll prime(ll n){
  
  ll a[12] = {2,3,5,7,11,13,17,19,23,29,31,37};
  if(n<=40){
    for(int i=0;i<12;i++){
      if(a[i]==n) return 1;
    }
    return 0;
  }
  ll d = n-1;
  while(d%2==0) d/=2;
  ll cnt = 0; 
  for(int i=0;i<12;i++){
    ll k = d;  
    if(pow(a[i],k,n)==1) cnt++;
    while(k<=n){
      if(pow(a[i],k,n)==n-1){
        cnt++;
        break;
      }
      k*=2;
    }
  }
  if(cnt==12) return 1;
  else return 0;
}

bool isSquare(ll n){
  ll l = 0;
  ll r = 1e9;
  ll mid = l+(r-l)/2;
  while(l+1<r){
    if(mid*mid==n) return true;
    if(mid*mid>n) r=mid;
    else l = mid;
    mid = l+(r-l)/2;
  }
  return false;
}

void solve(){
   ll n;
   cin>>n;
 
  vector<int> nums;
  int ans=0;
   for(int i=2;i<=1e6+1;i++){
    int cnt=0;
    while(n%i==0){
      n/=i;
      cnt++;
    }
    if(cnt!=0){
      ans+=cnt;
      nums.pb(cnt);
    }
    if(n<i) break;
   }
    if(prime(n)){
      ans++;
      nums.pb(1);
    }else if(n!=1){
      ans+=2;
      if(isSquare(n)){
        nums.pb(2);
      }else{
        nums.pb(1);
      }
    }

  ll res = 1;
  for(auto u:nums){
    res = (res*factorial(u))%mymod;
  }
  cout<<endl;
  int d = res;
  int x1,y1;
  int f = gcd(d,mymod,x1,y1);
  x1 = (x1+mymod)%mymod;
  ll myans = factorial(ans);
  myans = (myans*x1)%mymod;
  cout<<myans;
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

