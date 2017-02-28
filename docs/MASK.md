To create a mask and an outline image, start with the a picture
that you'd like to use for your project in GIMP or PhotoShop.

There's probably an easier way to do this, but this is how I do it.

![Cow 1](https://raw.githubusercontent.com/bibby/meat-cloud/master/docs/cow1.png)

Either on the original or on a duplicate layer, paint the background an unusual
color; something plainly not present in the original. We'll be doing a lot of
selection-inversion to get what we want.

The idea here is to select *just* the cow, and we'll do it by selecting
all of the *green*, and then inverting the selection (`Ctrl+I`).

![Cow 2](https://raw.githubusercontent.com/bibby/meat-cloud/master/docs/cow2.png)

Start a new black layer, and select the cow from the green layer (by selecting
the green, then inverting the selection). With the selection made, change layers
to the black layer and press delete. We now have a cutout of the image.

![Cow 3](https://raw.githubusercontent.com/bibby/meat-cloud/master/docs/cow3.png)

Take the time here to tidy up any artifacts; stray pixels and bleeding edges.
Make it a smooth cutout. The word cloud will avoid any pixels left in the
cutout, so occasionally select all black to see if anything is still inside.

Now we'll turn this negative image into a positive one. Start
another new black layer. Go to your cutout and select all the black.
Go to the new layer and press delete. Now you have a positive cow that you
can save as `mask.png` to use for the word cloud.

![Cow 4](https://raw.githubusercontent.com/bibby/meat-cloud/master/docs/cow4.png)

To create an outline, start a new layer just underneath the positive image.
From the cow layer, select all the black. Modify the selection using the *Grow*
option. Extend the selection by some number of pixels; here I did 4.

Go to the new empty layer and paint the selection white. You should see an
outlined cow.

![Cow 5](https://raw.githubusercontent.com/bibby/meat-cloud/master/docs/cow5.png)

But the white layer is solid, and we want it a line. So
back of the black cow layer, select all the black again. Go back to the white
layer and press delete. You now have an isolated outline.

![Cow 6](https://raw.githubusercontent.com/bibby/meat-cloud/master/docs/cow6.png)

Save this outline as `outline.png` to use with the word cloud to provide extra
structure to your final render.
