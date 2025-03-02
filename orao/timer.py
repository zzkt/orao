# -*- coding: utf-8 -*-

timer = {}
timer_pos = {}

def mem_listener(addr, val, cpu):
    if addr >= 0xA000 and addr <= 0xA0FF:
        timer_ix = addr & 0xFF
        if timer_ix in timer:
            print(
                (
                    "timer(%3d:%04x-%04x):duration %d cy"
                    % (
                        timer_ix,
                        timer_pos[timer_ix],
                        cpu.pc - 1,
                        cpu.cycles - timer[timer_ix] - 4,
                    )
                )
            )
            del timer[timer_ix]
            del timer_pos[timer_ix]
        else:
            timer[timer_ix] = cpu.cycles
            timer_pos[timer_ix] = cpu.pc + 2
