# MeatCloud

MeatCloud is an implementation of a wordcloud specifically for one T-shirt project
for Twitch.tv stream [BroBQ](https://www.twitch.tv/brobq). If you're looking for a
good time, watch BroBQ.

I have to dig for the repo that I borrowed a lot of code from, .. when I find it,
I'll update this to give credit. Meantime, sorry.

This project runs best with [docker](https://www.docker.com/), and has only been
used on Linux. It *should* run on OSX, but I can't confirm.

## Build

`./build`, if you don't mind the image name. Change the image used in 
`docker-compose.yml` if you pick something else.

## Preparing images

See this [Mask and Outline](https://github.com/bibby/meatcloud/blob/master/docs/README.md) document for tips on preparing a mask and outline image.

## Preparing for a render

You'll see placeholder directories `./in` and `./out`; The docker-compose file is
set to use these for input and output files respectively. See the [input readme](https://github.com/bibby/meatcloud/blob/master/in/README) for the specific expected file names.

## Render

View the parameters that the `./meat` script provides to inform what arguments are passed to docker-compose.
Or, check `./reroll`, which is just a lazy repeater for `./meat`.

## Example

![Meat Shirt](https://raw.githubusercontent.com/bibby/meatcloud/master/docs/MEAT_final.png)
