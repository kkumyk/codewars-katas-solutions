
function towerBuilder(nFloors) {
  var tower = [];
for (var floor = 0; floor < nFloors; floor++) {
tower.push(
  " ".repeat(nFloors - floor - 1) + 
  "*".repeat((floor * 2) + 1) + 
  " ".repeat(nFloors - floor - 1))
}
return tower;
}
