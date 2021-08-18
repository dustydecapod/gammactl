import click

from pydbus import SessionBus

# dbus setup
bus = SessionBus()
svc_proxy = bus.get('net.zoidplex.wlr_gamma_service',
        '/net/zoidplex/wlr_gamma_service')
brightnessctl = svc_proxy['net.zoidplex.wlr_gamma_service.brightness']
temperaturectl = svc_proxy['net.zoidplex.wlr_gamma_service.temperature']

_terse = False
_quiet = False
_as_percent = False

@click.group()
@click.option('--quiet', default=False, is_flag=True)
@click.option('--terse', default=False, is_flag=True)
def cli(quiet, terse):
    global _terse, _quiet
    _terse = terse
    _quiet = quiet

@cli.group()
@click.option('--as-percent', default=False, is_flag=True)
def brightness(as_percent):
    global _as_percent
    _as_percent = as_percent

@brightness.command()
def get():
    rval = round(brightnessctl.get(), 2)
    if _as_percent: rval = round(rval * 100)
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current brightness: %.2f" % rval)

@brightness.command()
@click.argument('value', default=1.0)
def set(value):
    if _as_percent: value /= 100.0
    rval = brightnessctl.set(value)
    if _as_percent: rval = round(rval * 100)
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current brightness: %.2f" % rval)

@brightness.command()
@click.argument('amount', default=0.05)
def increase(amount):
    if _as_percent: amount /= 100
    rval = brightnessctl.increase(amount)
    if _as_percent: rval = round(rval * 100)
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current brightness: %.2f" % rval)

@brightness.command()
@click.argument('amount', default=0.05)
def decrease(amount):
    if _as_percent: amount /= 100
    rval = brightnessctl.decrease(amount)
    if _as_percent: rval = round(rval * 100)
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current brightness: %.2f" % rval)

@cli.group()
def temperature():
    pass

@temperature.command()
def get():
    rval = temperaturectl.get()
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current temperature: %iK" % rval)

@temperature.command()
@click.argument('value', default=6500)
def set(value):
    rval = temperaturectl.set(value)
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current temperature: %iK" % rval)

@temperature.command()
@click.argument('amount', default=100)
def increase(amount):
    rval = temperaturectl.increase(amount)
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current temperature: %iK" % rval)

@temperature.command()
@click.argument('amount', default=100)
def decrease(amount):
    rval = temperaturectl.decrease(amount)
    if _quiet: return
    elif _terse: print(rval)
    else: print("Current temperature: %iK" % rval)

