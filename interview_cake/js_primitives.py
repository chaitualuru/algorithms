# <button id="btn-0">Button 1!</button>
# <button id="btn-1">Button 2!</button>
# <button id="btn-2">Button 3!</button>

# <script type="text/javascript">
#     var prizes = ['A Unicorn!', 'A Hug!', 'Fresh Laundry!'];
#     for (var btnNum = 0; btnNum < prizes.length; btnNum++) {
#         // for each of our buttons, when the user clicks it...
#         document.getElementById('btn-' + btnNum).onclick = function(frozenBtnNum){
#             return function() {
#                 // tell her what she's won!
#                 alert(prizes[frozenBtnNum]);
#             };
#         }(btnNum);
#     }
# </script>
# So when we pass btnNum to the outer anonymous function as its one argument,
# we create a new number inside the outer anonymous function called frozenBtnNum
# that has the value that btnNum had at that moment (0, 1, or 2).

# Our inner anonymous function is still a closure because it still 
# reaches outside its scope, but now it closes over this new number
# called frozenBtnNum, whose value will not change as we iterate 
# through our for loop.