# Parry This
## Description
Finally, learn how to be a samurai!

## Statement
Kuro is playing a new video game about samurai sword fighting. He is working on learning a new mechanic called **parrying**. In order to successfully parry an attack, Kuro must guard with his sword just before the enemy attack hits him. Specifically, he must guard within 30 frames of the attack landing - so if he guards at frame 0, any attack up to (*but not including*) frame 30 is defended. However, if the enemy's attack hits outside those 30 frames, then Kuro will *stagger*, leaving him vulnerable to damage for 60 frames - so if an attack staggers him at frame 100, any attack up to (*but not including*) frame 160 will deal damage.

You are given a list of all the frames that the guard button is pressed. You are also given a list of all the attacks from the enemy, along with the attack damage. Can you determine if Kuro will survive his fight, given his starting health?

Some notes about the mechanics:

* Kuro can only take damage while staggered, so the attack that staggers him does not deal damage.
* If Kuro attempts to guard while staggered, the guard will not take effect.
* Kuro can guard at any point while not staggered.
* If a guard and attack are performed simultaneously, the guard always wins.

The example case is shown in the image below:

![Sample Case](https://i.ibb.co/BGjKCmz/parry-this.png)

**NOTE**: 60 frames = 1 second in real time

<style>
img {
  max-width: 100%;
	  box-shadow: 0 0 8px 0 rgba(0, 0, 0, 0.3);
	}
</style>

## Input
The first line contains the integers **G**, **A**, and **H**: the number of guards, the number of attacks, and Kuro's starting health.

The next line contains **G** integers: the frames that Kuro guards, in sorted order.

The next line contains **A** integers: the frames that the enemy attacks, in sorted order.

The last line contains **A** integers: the damage that each attack will deal if it lands while Kuro is staggered.

## Output
If Kuro dies during the fight (health <= 0), output "Death". If Kuro survives, output one integer: the amount of health Kuro has remaining.

## Constraints
* 1 &le; **G, A, H** &le; 10<sup>5</sup>
* 0 &le; **frame** &le; 10<sup>6</sup>