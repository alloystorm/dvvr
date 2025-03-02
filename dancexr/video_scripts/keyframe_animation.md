In this video we are going to demonstrate the new keyframe animation feature. 

In 2025.3 update we introduced new feature that allows you to setup keyframes for almost all of the configurable values throughout the application. You can use it for almost everything from light settings to actor configuration to motion settings. 

This system is separate from the previous AutoUpdate feature where you can animate some values based on a few system inputs. You can still use the AutoUpdate system if you like.

Basically for the keyframe system, you can set a few different values at different times, and the system will automatically interpolate between those values when the timeline progresses. 

Let's use the overall intensity in the lighting configuration as an example. 

First we enable the keyframes for this configurations.

Then we move the timeline to 0, add a new keyframe and adjust the initial value.

Next we move the timeline a bit forward, add another keyframe and choose a different value.

Let's add a few more.

To select a keyframe you simply click on it and it will move timeline to that keyframe.

Then you can adjust the values using the value slider for that keyframe.

You cannot move keyframe to a different time but you can delete and create a new one.

Once you have your keyframes created, you can hit play and see the value changes through time.

You can also use keyframe for integer values. Like this light limit.

Let me animate it from 0 to 8. 

And you can see the lights turn on one-by-one.

You can also use it on selection values too. They will not interpolate but will change values when the time reaches the keyframe.

Let me open the fan motion demo to show you how that works.   

So the fan model here is loaded as an actor model so that it can be assigned a motion. 

Now with motion assigned the fan also needs to stay in the actor's hand, we can achieve that by using the "Attach To Actor" feature to bind the fan to the actor's hand. You need to select the actor and then a bone for the binding. 

Now this motion requires the fan to switch hands during the animation, previously this is impossible to do without interrupting the animation and change settings.

Here we can use the keyframe feature to set binding to a different bone at certain time. 

Like this, here we switch to left hand. 

And here we switch back to right hand.

So when the animation plays to these positions, the switching happens automatically.

That's it for this video, hope you now understand how the keyframe animation system works. 

Happy animating! See you next time!

