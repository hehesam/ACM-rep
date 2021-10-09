#include <bits/stdc++.h>
#include <algorithm>
#include<map>
#include<vector>
using namespace std;

struct drone{
  int pos;
  int speed;
  int id;
};

struct collision{
  int id1,id2;  
  double moment;
};

int n;
vector<drone> squad;
vector<collision> collide;

bool compareInterval(collision i1, collision i2) {
  return (i1.moment < i2.moment);
}

void checkForCollide() {
  // find crash moments
  for(int i = 0; i < squad.size(); i++){
    double posDiff = squad[i+1].pos - squad[i].pos;
    double speedDiff = squad[i+1].speed - squad[i].speed;
    
    if(speedDiff<0){
      collision bb;
      bb.id1 = squad[i].id;
      bb.id2 = squad[i+1].id;        
      bb.moment = posDiff/abs(speedDiff);
      collide.push_back(bb);
    }
  }

  if (collide.size() == 0) {
    return;
  }

  sort(collide.begin(), collide.end(), compareInterval);
  // remove drones with the minimum crash moments
  int min = -1;
  for(unsigned int i = 0;i < collide.size();i++){
    if ( min == -1 || min == collide[i].moment){
      min = collide[i].moment;
      int id1=collide[i].id1, id2=collide[i].id2;
      
      vector<drone>::iterator it;
      it = squad.begin() + id1 - 1;
      squad.erase(it);
      it = squad.begin() + id2 - 1;
      squad.erase(it);
    }
      else{
      break;           
    } 
  }
  collide.clear();

  checkForCollide();
}

int main(){
  cin >> n;
  // recieve drones
  for(int i=0;i<n;i++){
    drone aa;
    cin >> aa.pos >> aa.speed;
    aa.id = i+1;
    squad.push_back(aa);   
  }
  checkForCollide();
  cout << squad.size() << endl;
  for (int i = 0; i < squad.size(); i++) {
    cout << squad[i].id << endl;
  }
}
