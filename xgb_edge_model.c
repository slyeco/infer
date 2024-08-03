#include <math.h>
#include <string.h>
double sigmoid(double x) {
    if (x < 0.0) {
        double z = exp(x);
        return z / (1.0 + z);
    }
    return 1.0 / (1.0 + exp(-x));
}
void score(double * input, double * output) {
    double var0;
    if (input[6] < -0.87337124) {
        if (input[4] < -0.010208033) {
            if (input[5] < -0.009302213) {
                if (input[6] < -0.98452795) {
                    if (input[1] < -0.021532968) {
                        var0 = 0.0;
                    } else {
                        var0 = -0.54146343;
                    }
                } else {
                    if (input[8] < 0.036383152) {
                        if (input[3] < -1.2608186) {
                            if (input[0] < 2.303829) {
                                var0 = 0.54146343;
                            } else {
                                if (input[0] < 2.3099668) {
                                    var0 = 0.0;
                                } else {
                                    var0 = -0.52500004;
                                }
                            }
                        } else {
                            if (input[2] < -0.01849433) {
                                if (input[7] < 0.051915474) {
                                    var0 = 0.5345455;
                                } else {
                                    if (input[3] < -1.2183076) {
                                        var0 = 0.45000002;
                                    } else {
                                        if (input[2] < -0.025927046) {
                                            var0 = -0.3818182;
                                        } else {
                                            if (input[0] < 2.1983395) {
                                                var0 = 0.40000004;
                                            } else {
                                                var0 = -0.15;
                                            }
                                        }
                                    }
                                }
                            } else {
                                if (input[6] < -0.9590726) {
                                    var0 = -0.34285718;
                                } else {
                                    if (input[7] < 0.04953157) {
                                        if (input[7] < 0.03701756) {
                                            var0 = -0.16363637;
                                        } else {
                                            if (input[4] < -0.010669584) {
                                                if (input[5] < -0.013376542) {
                                                    var0 = 0.0;
                                                } else {
                                                    var0 = 0.4883721;
                                                }
                                            } else {
                                                var0 = 0.0;
                                            }
                                        }
                                    } else {
                                        if (input[6] < -0.9164384) {
                                            var0 = 0.15;
                                        } else {
                                            var0 = -0.40000004;
                                        }
                                    }
                                }
                            }
                        }
                    } else {
                        if (input[0] < 2.235474) {
                            if (input[1] < -0.02315183) {
                                if (input[6] < -0.9361422) {
                                    var0 = 0.36;
                                } else {
                                    if (input[0] < 2.2217367) {
                                        if (input[7] < 0.04921678) {
                                            var0 = -0.16363637;
                                        } else {
                                            var0 = -0.5555556;
                                        }
                                    } else {
                                        var0 = 0.0;
                                    }
                                }
                            } else {
                                if (input[3] < -1.1913816) {
                                    if (input[6] < -0.91386044) {
                                        var0 = -0.3818182;
                                    } else {
                                        if (input[2] < -0.034599453) {
                                            var0 = -0.33333337;
                                        } else {
                                            var0 = 0.34285718;
                                        }
                                    }
                                } else {
                                    var0 = 0.5172414;
                                }
                            }
                        } else {
                            if (input[2] < -0.035374377) {
                                var0 = 0.5409836;
                            } else {
                                if (input[8] < 0.04044383) {
                                    var0 = -0.42857146;
                                } else {
                                    var0 = 0.33333337;
                                }
                            }
                        }
                    }
                }
            } else {
                if (input[7] < 0.038667977) {
                    if (input[8] < 0.034556188) {
                        if (input[6] < -0.91104484) {
                            var0 = -0.5746479;
                        } else {
                            var0 = 0.0;
                        }
                    } else {
                        var0 = 0.24000001;
                    }
                } else {
                    if (input[2] < -0.018843733) {
                        if (input[2] < -0.026119491) {
                            if (input[3] < -1.2360004) {
                                var0 = 0.41538465;
                            } else {
                                if (input[0] < 2.164485) {
                                    var0 = 0.3;
                                } else {
                                    var0 = -0.53333336;
                                }
                            }
                        } else {
                            if (input[5] < -0.0067515816) {
                                if (input[6] < -0.95696956) {
                                    var0 = -0.15;
                                } else {
                                    var0 = 0.425;
                                }
                            } else {
                                if (input[1] < -0.025132062) {
                                    var0 = -0.40000004;
                                } else {
                                    var0 = 0.20000002;
                                }
                            }
                        }
                    } else {
                        if (input[0] < 2.0318189) {
                            if (input[3] < -1.0525924) {
                                var0 = 0.45000002;
                            } else {
                                var0 = -0.41538465;
                            }
                        } else {
                            if (input[8] < 0.039573204) {
                                if (input[2] < -0.01788577) {
                                    var0 = -0.120000005;
                                } else {
                                    var0 = -0.5166667;
                                }
                            } else {
                                var0 = 0.0;
                            }
                        }
                    }
                }
            }
        } else {
            if (input[6] < -0.9375794) {
                if (input[2] < -0.030995263) {
                    var0 = 0.20000002;
                } else {
                    if (input[2] < -0.027688757) {
                        if (input[3] < -1.2229909) {
                            var0 = 0.20000002;
                        } else {
                            var0 = -0.456;
                        }
                    } else {
                        var0 = -0.5941464;
                    }
                }
            } else {
                if (input[8] < 0.032759856) {
                    if (input[6] < -0.8902358) {
                        if (input[2] < -0.019408593) {
                            if (input[1] < -0.02682752) {
                                var0 = -0.42857146;
                            } else {
                                if (input[5] < -0.010071989) {
                                    var0 = 0.33333337;
                                } else {
                                    var0 = 0.0;
                                }
                            }
                        } else {
                            var0 = -0.52500004;
                        }
                    } else {
                        var0 = 0.20000002;
                    }
                } else {
                    if (input[1] < -0.023473276) {
                        if (input[8] < 0.041707657) {
                            var0 = -0.5;
                        } else {
                            var0 = 0.0;
                        }
                    } else {
                        if (input[3] < -1.0587685) {
                            if (input[2] < -0.029007493) {
                                var0 = -0.27272728;
                            } else {
                                if (input[2] < -0.015389477) {
                                    var0 = 0.44000003;
                                } else {
                                    if (input[3] < -1.107744) {
                                        var0 = -0.15;
                                    } else {
                                        var0 = 0.3;
                                    }
                                }
                            }
                        } else {
                            var0 = -0.3818182;
                        }
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.86050713) {
            if (input[3] < -1.1753037) {
                if (input[8] < 0.050490268) {
                    var0 = 0.5409836;
                } else {
                    var0 = 0.0;
                }
            } else {
                if (input[1] < -0.022404628) {
                    if (input[7] < 0.04953157) {
                        if (input[2] < -0.022673259) {
                            var0 = 0.33333337;
                        } else {
                            var0 = -0.3;
                        }
                    } else {
                        var0 = -0.5294118;
                    }
                } else {
                    var0 = 0.5;
                }
            }
        } else {
            var0 = 0.5967374;
        }
    }
    double var1;
    if (input[6] < -0.87337124) {
        if (input[5] < -0.009302213) {
            if (input[2] < -0.015711963) {
                if (input[4] < -0.008413696) {
                    if (input[8] < 0.036383152) {
                        if (input[6] < -0.98452795) {
                            if (input[7] < 0.03135134) {
                                var1 = -0.010847056;
                            } else {
                                var1 = -0.3719394;
                            }
                        } else {
                            if (input[1] < -0.027815487) {
                                if (input[2] < -0.03696189) {
                                    if (input[3] < -1.2522514) {
                                        var1 = 0.05012944;
                                    } else {
                                        var1 = 0.4200469;
                                    }
                                } else {
                                    if (input[1] < -0.029593235) {
                                        if (input[6] < -0.9662446) {
                                            var1 = -0.04310988;
                                        } else {
                                            var1 = -0.33248764;
                                        }
                                    } else {
                                        if (input[2] < -0.029493323) {
                                            var1 = 0.27882805;
                                        } else {
                                            var1 = -0.090552114;
                                        }
                                    }
                                }
                            } else {
                                if (input[6] < -0.9590726) {
                                    var1 = -0.23851207;
                                } else {
                                    if (input[7] < 0.050644714) {
                                        if (input[7] < 0.03701756) {
                                            if (input[5] < -0.011985467) {
                                                var1 = 0.384354;
                                            } else {
                                                var1 = -0.14939706;
                                            }
                                        } else {
                                            var1 = 0.4544705;
                                        }
                                    } else {
                                        if (input[2] < -0.020213827) {
                                            if (input[2] < -0.03318106) {
                                                if (input[0] < 2.2105289) {
                                                    var1 = -0.32676956;
                                                } else {
                                                    var1 = 0.2583465;
                                                }
                                            } else {
                                                if (input[6] < -0.9451282) {
                                                    var1 = -0.07214647;
                                                } else {
                                                    var1 = 0.39063385;
                                                }
                                            }
                                        } else {
                                            var1 = -0.30523866;
                                        }
                                    }
                                }
                            }
                        }
                    } else {
                        if (input[0] < 2.2244527) {
                            if (input[1] < -0.02315183) {
                                if (input[6] < -0.9361422) {
                                    var1 = 0.30163023;
                                } else {
                                    var1 = -0.41840795;
                                }
                            } else {
                                if (input[3] < -1.1913816) {
                                    if (input[6] < -0.91386044) {
                                        var1 = -0.35352606;
                                    } else {
                                        if (input[2] < -0.034599453) {
                                            var1 = -0.2842868;
                                        } else {
                                            var1 = 0.28990823;
                                        }
                                    }
                                } else {
                                    var1 = 0.38128185;
                                }
                            }
                        } else {
                            if (input[2] < -0.037807085) {
                                var1 = 0.43840128;
                            } else {
                                if (input[8] < 0.04044383) {
                                    if (input[6] < -0.9644232) {
                                        var1 = 0.08166998;
                                    } else {
                                        var1 = -0.4045577;
                                    }
                                } else {
                                    var1 = 0.3401249;
                                }
                            }
                        }
                    }
                } else {
                    if (input[0] < 2.1677947) {
                        var1 = 0.24952458;
                    } else {
                        if (input[6] < -0.92947114) {
                            var1 = -0.43793413;
                        } else {
                            if (input[6] < -0.8921962) {
                                var1 = 0.07216723;
                            } else {
                                var1 = -0.281978;
                            }
                        }
                    }
                }
            } else {
                if (input[0] < 2.0348344) {
                    if (input[3] < -1.0525924) {
                        var1 = 0.4326463;
                    } else {
                        var1 = -0.36708078;
                    }
                } else {
                    var1 = -0.44709587;
                }
            }
        } else {
            if (input[6] < -0.9429684) {
                if (input[4] < -0.0136898495) {
                    if (input[2] < -0.018843733) {
                        if (input[7] < 0.03639174) {
                            var1 = -0.17016199;
                        } else {
                            var1 = 0.3303986;
                        }
                    } else {
                        var1 = -0.4287802;
                    }
                } else {
                    var1 = -0.46230257;
                }
            } else {
                if (input[2] < -0.027172506) {
                    if (input[3] < -1.2223729) {
                        var1 = 0.062260542;
                    } else {
                        var1 = -0.44677836;
                    }
                } else {
                    if (input[8] < 0.033285618) {
                        if (input[6] < -0.8902358) {
                            if (input[3] < -1.205431) {
                                var1 = 0.18189557;
                            } else {
                                if (input[2] < -0.01788577) {
                                    if (input[3] < -1.1929682) {
                                        var1 = -0.42137936;
                                    } else {
                                        if (input[2] < -0.020644043) {
                                            var1 = -0.05986149;
                                        } else {
                                            var1 = 0.3686957;
                                        }
                                    }
                                } else {
                                    if (input[1] < -0.023473276) {
                                        var1 = -0.02829587;
                                    } else {
                                        if (input[6] < -0.89445615) {
                                            var1 = -0.42379048;
                                        } else {
                                            var1 = -0.065599084;
                                        }
                                    }
                                }
                            }
                        } else {
                            if (input[0] < 1.998746) {
                                var1 = -0.0771577;
                            } else {
                                var1 = 0.25844002;
                            }
                        }
                    } else {
                        if (input[1] < -0.025132062) {
                            if (input[8] < 0.041872345) {
                                var1 = -0.30353725;
                            } else {
                                var1 = 0.20501128;
                            }
                        } else {
                            if (input[3] < -1.0609391) {
                                if (input[2] < -0.01659909) {
                                    if (input[8] < 0.04059853) {
                                        var1 = 0.42317244;
                                    } else {
                                        var1 = 0.06504963;
                                    }
                                } else {
                                    if (input[3] < -1.1056226) {
                                        var1 = -0.21167758;
                                    } else {
                                        var1 = 0.35462546;
                                    }
                                }
                            } else {
                                var1 = -0.29767102;
                            }
                        }
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            if (input[3] < -1.1753037) {
                if (input[8] < 0.04700461) {
                    var1 = 0.44055486;
                } else {
                    var1 = 0.07965605;
                }
            } else {
                if (input[1] < -0.022404628) {
                    if (input[0] < 2.0613148) {
                        var1 = 0.32072327;
                    } else {
                        if (input[7] < 0.04953157) {
                            if (input[0] < 2.0963252) {
                                var1 = -0.31053147;
                            } else {
                                var1 = 0.1609377;
                            }
                        } else {
                            var1 = -0.43528435;
                        }
                    }
                } else {
                    var1 = 0.39746183;
                }
            }
        } else {
            var1 = 0.46406683;
        }
    }
    double var2;
    if (input[6] < -0.87337124) {
        if (input[4] < -0.010208033) {
            if (input[2] < -0.015711963) {
                if (input[5] < -0.008279108) {
                    if (input[3] < -1.1622715) {
                        if (input[2] < -0.038976364) {
                            if (input[1] < -0.028228225) {
                                var2 = 0.38058975;
                            } else {
                                if (input[4] < -0.015655592) {
                                    var2 = -0.24929567;
                                } else {
                                    var2 = 0.18699104;
                                }
                            }
                        } else {
                            if (input[7] < 0.051451307) {
                                if (input[6] < -0.9590726) {
                                    if (input[7] < 0.048279554) {
                                        var2 = -0.3942468;
                                    } else {
                                        if (input[8] < 0.03291272) {
                                            var2 = -0.10479502;
                                        } else {
                                            var2 = 0.33789244;
                                        }
                                    }
                                } else {
                                    if (input[0] < 2.316065) {
                                        if (input[8] < 0.037544537) {
                                            if (input[3] < -1.205431) {
                                                if (input[8] < 0.035528053) {
                                                    var2 = 0.39492458;
                                                } else {
                                                    var2 = 0.03572978;
                                                }
                                            } else {
                                                if (input[3] < -1.1913816) {
                                                    var2 = -0.1969585;
                                                } else {
                                                    var2 = 0.29190814;
                                                }
                                            }
                                        } else {
                                            if (input[8] < 0.043192063) {
                                                if (input[3] < -1.1913816) {
                                                    var2 = -0.2299832;
                                                } else {
                                                    var2 = 0.24956529;
                                                }
                                            } else {
                                                var2 = 0.3968587;
                                            }
                                        }
                                    } else {
                                        var2 = -0.33801502;
                                    }
                                }
                            } else {
                                if (input[6] < -0.90437704) {
                                    if (input[7] < 0.05393495) {
                                        if (input[4] < -0.013251005) {
                                            var2 = -0.36549193;
                                        } else {
                                            var2 = 0.09220436;
                                        }
                                    } else {
                                        var2 = 0.35650912;
                                    }
                                } else {
                                    if (input[1] < -0.02166582) {
                                        if (input[1] < -0.04030086) {
                                            var2 = 0.049872655;
                                        } else {
                                            var2 = -0.37500012;
                                        }
                                    } else {
                                        var2 = 0.133354;
                                    }
                                }
                            }
                        }
                    } else {
                        if (input[1] < -0.022539979) {
                            if (input[3] < -1.1364958) {
                                var2 = 0.28745565;
                            } else {
                                var2 = -0.19180726;
                            }
                        } else {
                            var2 = 0.40180588;
                        }
                    }
                } else {
                    if (input[0] < 2.130947) {
                        if (input[7] < 0.038667977) {
                            var2 = -0.081564434;
                        } else {
                            var2 = 0.3138087;
                        }
                    } else {
                        if (input[3] < -1.2242881) {
                            if (input[6] < -0.95542103) {
                                if (input[7] < 0.036118194) {
                                    var2 = -0.31249142;
                                } else {
                                    var2 = 0.029158738;
                                }
                            } else {
                                var2 = 0.37604085;
                            }
                        } else {
                            if (input[8] < 0.042523675) {
                                var2 = -0.35052034;
                            } else {
                                var2 = 0.08594046;
                            }
                        }
                    }
                }
            } else {
                if (input[0] < 2.0348344) {
                    if (input[3] < -1.0525924) {
                        var2 = 0.38392177;
                    } else {
                        var2 = -0.34043908;
                    }
                } else {
                    var2 = -0.37571666;
                }
            }
        } else {
            if (input[7] < 0.03985398) {
                var2 = -0.4003334;
            } else {
                if (input[3] < -1.2204049) {
                    if (input[6] < -0.9822939) {
                        var2 = -0.27233303;
                    } else {
                        var2 = 0.37272432;
                    }
                } else {
                    if (input[3] < -1.1707715) {
                        if (input[1] < -0.020601308) {
                            var2 = -0.38015768;
                        } else {
                            if (input[6] < -0.9500209) {
                                var2 = -0.2793222;
                            } else {
                                var2 = 0.18484156;
                            }
                        }
                    } else {
                        if (input[2] < -0.014220504) {
                            if (input[1] < -0.012812677) {
                                if (input[6] < -0.9451282) {
                                    var2 = -0.08850719;
                                } else {
                                    var2 = 0.31566322;
                                }
                            } else {
                                var2 = -0.26751226;
                            }
                        } else {
                            if (input[6] < -0.8902358) {
                                var2 = -0.3525627;
                            } else {
                                var2 = 0.072557755;
                            }
                        }
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            if (input[3] < -1.1753037) {
                if (input[8] < 0.04700461) {
                    var2 = 0.37834692;
                } else {
                    var2 = 0.063970104;
                }
            } else {
                if (input[1] < -0.022404628) {
                    if (input[0] < 2.0613148) {
                        var2 = 0.27673262;
                    } else {
                        if (input[8] < 0.035254806) {
                            var2 = -0.04972828;
                        } else {
                            var2 = -0.3584198;
                        }
                    }
                } else {
                    var2 = 0.33494133;
                }
            }
        } else {
            var2 = 0.4026937;
        }
    }
    double var3;
    if (input[6] < -0.87337124) {
        if (input[7] < 0.03783055) {
            if (input[4] < -0.013563801) {
                if (input[1] < -0.013988943) {
                    if (input[5] < -0.0069732172) {
                        if (input[6] < -0.95696956) {
                            var3 = -0.028965885;
                        } else {
                            var3 = 0.34542966;
                        }
                    } else {
                        var3 = -0.15040946;
                    }
                } else {
                    var3 = -0.3184032;
                }
            } else {
                var3 = -0.36469468;
            }
        } else {
            if (input[2] < -0.014220504) {
                if (input[0] < 2.2311826) {
                    if (input[2] < -0.026119491) {
                        if (input[0] < 2.1247864) {
                            var3 = 0.24972066;
                        } else {
                            if (input[1] < -0.020236952) {
                                if (input[4] < -0.013395523) {
                                    if (input[7] < 0.05160624) {
                                        if (input[5] < -0.008441541) {
                                            var3 = 0.27969718;
                                        } else {
                                            var3 = -0.13065715;
                                        }
                                    } else {
                                        var3 = -0.29078078;
                                    }
                                } else {
                                    var3 = -0.36478695;
                                }
                            } else {
                                if (input[6] < -0.9244476) {
                                    var3 = -0.08339767;
                                } else {
                                    var3 = 0.22193982;
                                }
                            }
                        }
                    } else {
                        if (input[6] < -0.94176215) {
                            if (input[7] < 0.051066376) {
                                var3 = -0.34595567;
                            } else {
                                var3 = -0.018937422;
                            }
                        } else {
                            if (input[1] < -0.025132062) {
                                if (input[8] < 0.041004214) {
                                    if (input[6] < -0.88553137) {
                                        if (input[5] < -0.011754653) {
                                            var3 = 0.0067317304;
                                        } else {
                                            var3 = -0.32191774;
                                        }
                                    } else {
                                        var3 = 0.02719176;
                                    }
                                } else {
                                    if (input[6] < -0.89710027) {
                                        var3 = 0.29416373;
                                    } else {
                                        var3 = -0.27974108;
                                    }
                                }
                            } else {
                                if (input[1] < -0.011652317) {
                                    if (input[4] < -0.017901432) {
                                        if (input[6] < -0.9244476) {
                                            var3 = -0.27051514;
                                        } else {
                                            var3 = 0.046439443;
                                        }
                                    } else {
                                        if (input[5] < -0.0076379003) {
                                            if (input[8] < 0.027336787) {
                                                var3 = -0.023494286;
                                            } else {
                                                if (input[5] < -0.013959031) {
                                                    var3 = 0.07058728;
                                                } else {
                                                    var3 = 0.3183805;
                                                }
                                            }
                                        } else {
                                            if (input[1] < -0.019719763) {
                                                var3 = 0.20729242;
                                            } else {
                                                if (input[0] < 2.084277) {
                                                    var3 = 0.12568495;
                                                } else {
                                                    var3 = -0.25278765;
                                                }
                                            }
                                        }
                                    }
                                } else {
                                    var3 = -0.26510614;
                                }
                            }
                        }
                    }
                } else {
                    if (input[6] < -0.9784445) {
                        if (input[1] < -0.03048607) {
                            var3 = 0.21440262;
                        } else {
                            var3 = -0.34358343;
                        }
                    } else {
                        if (input[7] < 0.03898465) {
                            var3 = -0.18909658;
                        } else {
                            if (input[3] < -1.2566861) {
                                if (input[0] < 2.303829) {
                                    var3 = 0.36479098;
                                } else {
                                    if (input[5] < -0.011560104) {
                                        var3 = -0.37228897;
                                    } else {
                                        var3 = 0.086071536;
                                    }
                                }
                            } else {
                                if (input[7] < 0.0407903) {
                                    if (input[6] < -0.9590726) {
                                        var3 = -0.13278277;
                                    } else {
                                        var3 = 0.22126828;
                                    }
                                } else {
                                    var3 = 0.3700683;
                                }
                            }
                        }
                    }
                }
            } else {
                if (input[3] < -1.0963953) {
                    var3 = -0.35595518;
                } else {
                    if (input[3] < -1.0525924) {
                        var3 = 0.34485638;
                    } else {
                        var3 = -0.35304287;
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            if (input[3] < -1.1753037) {
                if (input[8] < 0.04700461) {
                    var3 = 0.33986172;
                } else {
                    var3 = 0.05140873;
                }
            } else {
                if (input[1] < -0.022404628) {
                    if (input[0] < 2.0613148) {
                        var3 = 0.24388036;
                    } else {
                        if (input[7] < 0.04953157) {
                            if (input[3] < -1.1299331) {
                                var3 = 0.18210961;
                            } else {
                                var3 = -0.24770962;
                            }
                        } else {
                            var3 = -0.32392246;
                        }
                    }
                } else {
                    var3 = 0.29198688;
                }
            }
        } else {
            var3 = 0.36810094;
        }
    }
    double var4;
    if (input[6] < -0.8662804) {
        if (input[5] < -0.009302213) {
            if (input[2] < -0.015711963) {
                if (input[2] < -0.038976364) {
                    if (input[1] < -0.028228225) {
                        var4 = 0.32125315;
                    } else {
                        if (input[4] < -0.015562298) {
                            var4 = -0.15194866;
                        } else {
                            var4 = 0.18199432;
                        }
                    }
                } else {
                    if (input[1] < -0.026398363) {
                        if (input[0] < 2.2244527) {
                            if (input[7] < 0.045210462) {
                                if (input[4] < -0.011879761) {
                                    var4 = 0.236677;
                                } else {
                                    var4 = -0.24558096;
                                }
                            } else {
                                var4 = -0.30813408;
                            }
                        } else {
                            if (input[6] < -0.9339922) {
                                if (input[3] < -1.2566861) {
                                    if (input[0] < 2.303829) {
                                        var4 = 0.2393199;
                                    } else {
                                        var4 = -0.33249062;
                                    }
                                } else {
                                    if (input[0] < 2.2558458) {
                                        var4 = -0.23102267;
                                    } else {
                                        var4 = 0.29894483;
                                    }
                                }
                            } else {
                                var4 = 0.29586232;
                            }
                        }
                    } else {
                        if (input[6] < -0.9590726) {
                            var4 = -0.2782991;
                        } else {
                            if (input[8] < 0.03768708) {
                                if (input[4] < -0.008334108) {
                                    if (input[7] < 0.05042656) {
                                        if (input[4] < -0.018492304) {
                                            var4 = -0.025769336;
                                        } else {
                                            var4 = 0.3105808;
                                        }
                                    } else {
                                        if (input[2] < -0.01924576) {
                                            if (input[2] < -0.031958528) {
                                                if (input[0] < 2.2105289) {
                                                    var4 = -0.24311125;
                                                } else {
                                                    var4 = 0.21086259;
                                                }
                                            } else {
                                                if (input[5] < -0.010071989) {
                                                    var4 = 0.29006985;
                                                } else {
                                                    var4 = -0.06471233;
                                                }
                                            }
                                        } else {
                                            var4 = -0.20139669;
                                        }
                                    }
                                } else {
                                    if (input[1] < -0.021402339) {
                                        var4 = -0.29688618;
                                    } else {
                                        var4 = 0.15200052;
                                    }
                                }
                            } else {
                                if (input[0] < 2.1788154) {
                                    if (input[1] < -0.023636326) {
                                        var4 = -0.10036886;
                                    } else {
                                        var4 = 0.27802637;
                                    }
                                } else {
                                    if (input[4] < -0.012763074) {
                                        var4 = 0.057934873;
                                    } else {
                                        var4 = -0.3005359;
                                    }
                                }
                            }
                        }
                    }
                }
            } else {
                if (input[0] < 2.0348344) {
                    if (input[3] < -1.0525924) {
                        var4 = 0.30224466;
                    } else {
                        var4 = -0.23164259;
                    }
                } else {
                    var4 = -0.3074122;
                }
            }
        } else {
            if (input[6] < -0.9439412) {
                if (input[2] < -0.030199764) {
                    var4 = 0.08184248;
                } else {
                    if (input[7] < 0.039404217) {
                        var4 = -0.34662178;
                    } else {
                        if (input[3] < -1.224942) {
                            if (input[6] < -0.9644232) {
                                var4 = -0.2750235;
                            } else {
                                var4 = 0.30496785;
                            }
                        } else {
                            var4 = -0.30693907;
                        }
                    }
                }
            } else {
                if (input[4] < -0.011109029) {
                    if (input[7] < 0.047997124) {
                        if (input[5] < -0.0076379003) {
                            if (input[1] < -0.022682095) {
                                var4 = -0.04106099;
                            } else {
                                var4 = 0.24269386;
                            }
                        } else {
                            if (input[8] < 0.042296365) {
                                if (input[0] < 2.0290835) {
                                    var4 = 0.12706216;
                                } else {
                                    if (input[3] < -1.201232) {
                                        var4 = 0.09398202;
                                    } else {
                                        var4 = -0.252214;
                                    }
                                }
                            } else {
                                var4 = 0.22889833;
                            }
                        }
                    } else {
                        if (input[2] < -0.018843733) {
                            if (input[2] < -0.028549777) {
                                var4 = -0.24129006;
                            } else {
                                var4 = 0.16016242;
                            }
                        } else {
                            var4 = -0.28698722;
                        }
                    }
                } else {
                    if (input[6] < -0.8892233) {
                        if (input[8] < 0.034149013) {
                            var4 = -0.29202807;
                        } else {
                            if (input[2] < -0.022673259) {
                                var4 = -0.23480134;
                            } else {
                                if (input[2] < -0.013142619) {
                                    var4 = 0.1943204;
                                } else {
                                    var4 = -0.14090666;
                                }
                            }
                        }
                    } else {
                        var4 = 0.120582625;
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            if (input[7] < 0.05348195) {
                var4 = 0.2705425;
            } else {
                if (input[3] < -1.1753037) {
                    var4 = 0.24349678;
                } else {
                    var4 = -0.22602344;
                }
            }
        } else {
            var4 = 0.34644568;
        }
    }
    double var5;
    if (input[6] < -0.8626252) {
        if (input[7] < 0.03701756) {
            if (input[2] < -0.028193833) {
                if (input[4] < -0.014463788) {
                    var5 = 0.28960893;
                } else {
                    var5 = -0.12373457;
                }
            } else {
                if (input[6] < -0.91386044) {
                    if (input[8] < 0.03602988) {
                        var5 = -0.33297086;
                    } else {
                        var5 = 0.048085462;
                    }
                } else {
                    var5 = 0.11678525;
                }
            }
        } else {
            if (input[2] < -0.014220504) {
                if (input[0] < 2.2311826) {
                    if (input[1] < -0.022404628) {
                        if (input[7] < 0.05160624) {
                            if (input[4] < -0.012567718) {
                                if (input[3] < -1.1364958) {
                                    if (input[7] < 0.04978312) {
                                        if (input[5] < -0.0064001516) {
                                            var5 = 0.31616643;
                                        } else {
                                            var5 = -0.04058317;
                                        }
                                    } else {
                                        var5 = -0.059180602;
                                    }
                                } else {
                                    var5 = -0.13855615;
                                }
                            } else {
                                if (input[8] < 0.041872345) {
                                    if (input[5] < -0.011560104) {
                                        if (input[5] < -0.013822603) {
                                            var5 = -0.20885563;
                                        } else {
                                            var5 = 0.21427894;
                                        }
                                    } else {
                                        if (input[7] < 0.04672999) {
                                            var5 = -0.3274942;
                                        } else {
                                            if (input[6] < -0.9074173) {
                                                if (input[0] < 2.2011743) {
                                                    var5 = 0.26169196;
                                                } else {
                                                    var5 = -0.14716065;
                                                }
                                            } else {
                                                var5 = -0.26770428;
                                            }
                                        }
                                    }
                                } else {
                                    var5 = 0.20206271;
                                }
                            }
                        } else {
                            if (input[8] < 0.034556188) {
                                if (input[7] < 0.052231286) {
                                    var5 = -0.10995904;
                                } else {
                                    var5 = 0.27518135;
                                }
                            } else {
                                if (input[7] < 0.05746478) {
                                    var5 = -0.321963;
                                } else {
                                    if (input[1] < -0.03384914) {
                                        var5 = 0.14157514;
                                    } else {
                                        var5 = -0.20625521;
                                    }
                                }
                            }
                        }
                    } else {
                        if (input[6] < -0.94694364) {
                            var5 = -0.31429675;
                        } else {
                            if (input[3] < -1.1913816) {
                                if (input[6] < -0.91386044) {
                                    if (input[3] < -1.2079631) {
                                        var5 = 0.22351506;
                                    } else {
                                        var5 = -0.4268898;
                                    }
                                } else {
                                    if (input[2] < -0.028754959) {
                                        var5 = -0.15195195;
                                    } else {
                                        var5 = 0.32079926;
                                    }
                                }
                            } else {
                                if (input[1] < -0.011652317) {
                                    if (input[5] < -0.007465656) {
                                        if (input[4] < -0.007539364) {
                                            var5 = 0.31673706;
                                        } else {
                                            var5 = -0.013071278;
                                        }
                                    } else {
                                        var5 = -0.00439355;
                                    }
                                } else {
                                    var5 = -0.19153461;
                                }
                            }
                        }
                    }
                } else {
                    if (input[6] < -0.9769194) {
                        if (input[2] < -0.037253346) {
                            var5 = 0.21041231;
                        } else {
                            var5 = -0.30219167;
                        }
                    } else {
                        if (input[0] < 2.3050196) {
                            if (input[6] < -0.9522211) {
                                if (input[7] < 0.0407903) {
                                    var5 = -0.14150032;
                                } else {
                                    var5 = 0.26718;
                                }
                            } else {
                                var5 = 0.32099614;
                            }
                        } else {
                            if (input[3] < -1.2566861) {
                                if (input[7] < 0.04426297) {
                                    var5 = 0.06420143;
                                } else {
                                    var5 = -0.30824712;
                                }
                            } else {
                                var5 = 0.30915666;
                            }
                        }
                    }
                }
            } else {
                if (input[3] < -1.0963953) {
                    var5 = -0.3122743;
                } else {
                    if (input[3] < -1.049708) {
                        var5 = 0.28045756;
                    } else {
                        var5 = -0.30538717;
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            if (input[0] < 2.1030936) {
                var5 = 0.2518864;
            } else {
                if (input[3] < -1.178581) {
                    var5 = 0.20324694;
                } else {
                    var5 = -0.22541988;
                }
            }
        } else {
            var5 = 0.3319807;
        }
    }
    double var6;
    if (input[6] < -0.8626252) {
        if (input[6] < -0.9590726) {
            if (input[2] < -0.03318106) {
                var6 = 0.25166774;
            } else {
                var6 = -0.3198436;
            }
        } else {
            if (input[0] < 2.2542195) {
                if (input[6] < -0.9461092) {
                    var6 = -0.31226;
                } else {
                    if (input[4] < -0.010669584) {
                        if (input[7] < 0.04953157) {
                            if (input[5] < -0.0077787093) {
                                if (input[3] < -1.1350421) {
                                    if (input[3] < -1.1913816) {
                                        if (input[3] < -1.205431) {
                                            var6 = 0.25758162;
                                        } else {
                                            if (input[6] < -0.9164384) {
                                                var6 = -0.32379565;
                                            } else {
                                                var6 = 0.14834277;
                                            }
                                        }
                                    } else {
                                        var6 = 0.32152474;
                                    }
                                } else {
                                    if (input[7] < 0.045833576) {
                                        if (input[3] < -1.131417) {
                                            var6 = -0.079950035;
                                        } else {
                                            var6 = 0.25381833;
                                        }
                                    } else {
                                        if (input[1] < -0.022404628) {
                                            var6 = -0.27239048;
                                        } else {
                                            var6 = 0.063032426;
                                        }
                                    }
                                }
                            } else {
                                if (input[3] < -1.1900722) {
                                    var6 = -0.17350645;
                                } else {
                                    if (input[0] < 2.1173608) {
                                        if (input[0] < 2.0290835) {
                                            var6 = 0.07963634;
                                        } else {
                                            var6 = -0.23514976;
                                        }
                                    } else {
                                        var6 = 0.23318855;
                                    }
                                }
                            }
                        } else {
                            if (input[0] < 2.2217367) {
                                if (input[1] < -0.02166582) {
                                    if (input[8] < 0.037544537) {
                                        if (input[4] < -0.012691641) {
                                            if (input[0] < 2.1956103) {
                                                var6 = -0.055734355;
                                            } else {
                                                var6 = 0.26178715;
                                            }
                                        } else {
                                            var6 = -0.19096436;
                                        }
                                    } else {
                                        var6 = -0.3093545;
                                    }
                                } else {
                                    if (input[8] < 0.033171043) {
                                        var6 = -0.16710721;
                                    } else {
                                        var6 = 0.2546616;
                                    }
                                }
                            } else {
                                if (input[3] < -1.2360004) {
                                    var6 = -0.042051513;
                                } else {
                                    var6 = 0.26610342;
                                }
                            }
                        }
                    } else {
                        if (input[6] < -0.88553137) {
                            if (input[1] < -0.025790757) {
                                var6 = -0.28152213;
                            } else {
                                if (input[2] < -0.01528149) {
                                    if (input[6] < -0.9074173) {
                                        if (input[8] < 0.03142541) {
                                            if (input[7] < 0.047196794) {
                                                var6 = -0.2751666;
                                            } else {
                                                var6 = 0.17135;
                                            }
                                        } else {
                                            if (input[2] < -0.025525229) {
                                                var6 = -0.039244134;
                                            } else {
                                                var6 = 0.24510604;
                                            }
                                        }
                                    } else {
                                        if (input[1] < -0.020601308) {
                                            var6 = -0.2719477;
                                        } else {
                                            if (input[8] < 0.030414678) {
                                                var6 = -0.16334745;
                                            } else {
                                                var6 = 0.1767779;
                                            }
                                        }
                                    }
                                } else {
                                    var6 = -0.22653057;
                                }
                            }
                        } else {
                            if (input[5] < -0.01573221) {
                                var6 = -0.27593216;
                            } else {
                                var6 = 0.25319672;
                            }
                        }
                    }
                }
            } else {
                if (input[0] < 2.3120162) {
                    if (input[6] < -0.95696956) {
                        var6 = -0.032322627;
                    } else {
                        var6 = 0.30243167;
                    }
                } else {
                    if (input[3] < -1.2590284) {
                        var6 = -0.25934437;
                    } else {
                        var6 = 0.18636145;
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            var6 = 0.11613238;
        } else {
            var6 = 0.32183307;
        }
    }
    double var7;
    if (input[6] < -0.8662804) {
        if (input[7] < 0.03701756) {
            if (input[4] < -0.0136487745) {
                if (input[5] < -0.011985467) {
                    var7 = 0.25434268;
                } else {
                    if (input[1] < -0.021735445) {
                        var7 = 0.087880224;
                    } else {
                        var7 = -0.19734189;
                    }
                }
            } else {
                var7 = -0.3102057;
            }
        } else {
            if (input[2] < -0.017490756) {
                if (input[0] < 2.1270807) {
                    if (input[4] < -0.016673163) {
                        var7 = -0.12650718;
                    } else {
                        if (input[4] < -0.00788809) {
                            var7 = 0.27411407;
                        } else {
                            var7 = -0.044406135;
                        }
                    }
                } else {
                    if (input[0] < 2.2288184) {
                        if (input[2] < -0.026119491) {
                            if (input[1] < -0.020236952) {
                                if (input[3] < -1.2292796) {
                                    if (input[7] < 0.05348195) {
                                        var7 = 0.17237751;
                                    } else {
                                        var7 = -0.21355861;
                                    }
                                } else {
                                    var7 = -0.24242388;
                                }
                            } else {
                                var7 = 0.09828394;
                            }
                        } else {
                            if (input[3] < -1.205431) {
                                if (input[6] < -0.9339922) {
                                    var7 = -0.20119815;
                                } else {
                                    var7 = 0.2949479;
                                }
                            } else {
                                if (input[3] < -1.1913816) {
                                    if (input[6] < -0.91386044) {
                                        var7 = -0.33409786;
                                    } else {
                                        var7 = 0.20001839;
                                    }
                                } else {
                                    if (input[7] < 0.051267665) {
                                        if (input[6] < -0.9461092) {
                                            var7 = -0.1752177;
                                        } else {
                                            var7 = 0.27367282;
                                        }
                                    } else {
                                        var7 = -0.1557978;
                                    }
                                }
                            }
                        }
                    } else {
                        if (input[2] < -0.0197182) {
                            if (input[3] < -1.2566861) {
                                if (input[0] < 2.303829) {
                                    var7 = 0.26983094;
                                } else {
                                    var7 = -0.22492854;
                                }
                            } else {
                                if (input[3] < -1.2229909) {
                                    var7 = 0.26242518;
                                } else {
                                    if (input[6] < -0.9451282) {
                                        var7 = -0.20945436;
                                    } else {
                                        var7 = 0.21611933;
                                    }
                                }
                            }
                        } else {
                            var7 = -0.13813491;
                        }
                    }
                }
            } else {
                if (input[3] < -1.0963953) {
                    if (input[1] < -0.017355837) {
                        if (input[6] < -0.9074173) {
                            if (input[6] < -0.9644232) {
                                var7 = -0.20597276;
                            } else {
                                if (input[7] < 0.03808883) {
                                    var7 = -0.16441461;
                                } else {
                                    var7 = 0.20116107;
                                }
                            }
                        } else {
                            if (input[3] < -1.1281893) {
                                var7 = -0.30521947;
                            } else {
                                var7 = 0.10929937;
                            }
                        }
                    } else {
                        var7 = -0.28263605;
                    }
                } else {
                    if (input[3] < -1.0525924) {
                        var7 = 0.2866935;
                    } else {
                        var7 = -0.25690657;
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            if (input[1] < -0.024021015) {
                if (input[2] < -0.034599453) {
                    var7 = 0.2186074;
                } else {
                    var7 = -0.19166802;
                }
            } else {
                var7 = 0.23475571;
            }
        } else {
            var7 = 0.31437922;
        }
    }
    double var8;
    if (input[6] < -0.8626252) {
        if (input[6] < -0.9590726) {
            if (input[2] < -0.03563804) {
                var8 = 0.24979065;
            } else {
                if (input[7] < 0.048279554) {
                    var8 = -0.30657816;
                } else {
                    var8 = 0.016727295;
                }
            }
        } else {
            if (input[0] < 2.2542195) {
                if (input[6] < -0.9461092) {
                    var8 = -0.28620395;
                } else {
                    if (input[1] < -0.02166582) {
                        if (input[2] < -0.03696189) {
                            if (input[1] < -0.029346257) {
                                var8 = 0.2520678;
                            } else {
                                var8 = -0.03826105;
                            }
                        } else {
                            if (input[6] < -0.89921194) {
                                if (input[0] < 2.2105289) {
                                    if (input[4] < -0.012805835) {
                                        var8 = 0.2704506;
                                    } else {
                                        if (input[6] < -0.9074173) {
                                            if (input[7] < 0.044517975) {
                                                var8 = -0.03348381;
                                            } else {
                                                var8 = 0.24471757;
                                            }
                                        } else {
                                            var8 = -0.14633854;
                                        }
                                    }
                                } else {
                                    if (input[6] < -0.9339922) {
                                        var8 = -0.27488682;
                                    } else {
                                        var8 = 0.03894042;
                                    }
                                }
                            } else {
                                if (input[7] < 0.05042656) {
                                    if (input[3] < -1.1434832) {
                                        if (input[2] < -0.030764878) {
                                            var8 = -0.10254432;
                                        } else {
                                            var8 = 0.2568332;
                                        }
                                    } else {
                                        if (input[0] < 2.0884235) {
                                            var8 = 0.024207816;
                                        } else {
                                            var8 = -0.30597237;
                                        }
                                    }
                                } else {
                                    var8 = -0.23775196;
                                }
                            }
                        }
                    } else {
                        if (input[2] < -0.015711963) {
                            if (input[0] < 2.1755462) {
                                var8 = 0.23052187;
                            } else {
                                if (input[3] < -1.205431) {
                                    if (input[2] < -0.027688757) {
                                        var8 = -0.08547371;
                                    } else {
                                        var8 = 0.20448963;
                                    }
                                } else {
                                    if (input[3] < -1.1913816) {
                                        if (input[6] < -0.9164384) {
                                            var8 = -0.33705887;
                                        } else {
                                            var8 = -0.00339145;
                                        }
                                    } else {
                                        var8 = 0.19744328;
                                    }
                                }
                            }
                        } else {
                            if (input[6] < -0.89445615) {
                                if (input[1] < -0.018689357) {
                                    var8 = 0.06907987;
                                } else {
                                    var8 = -0.2399093;
                                }
                            } else {
                                if (input[3] < -1.049708) {
                                    var8 = 0.22815365;
                                } else {
                                    var8 = -0.1934985;
                                }
                            }
                        }
                    }
                }
            } else {
                if (input[0] < 2.3050196) {
                    if (input[6] < -0.95542103) {
                        var8 = -0.0121629825;
                    } else {
                        var8 = 0.2976229;
                    }
                } else {
                    if (input[3] < -1.2566861) {
                        var8 = -0.15585929;
                    } else {
                        var8 = 0.17815885;
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            var8 = 0.089566715;
        } else {
            var8 = 0.30861083;
        }
    }
    double var9;
    if (input[6] < -0.86785334) {
        if (input[6] < -0.9644232) {
            if (input[2] < -0.03318106) {
                var9 = 0.20456634;
            } else {
                var9 = -0.3048983;
            }
        } else {
            if (input[5] < -0.009302213) {
                if (input[4] < -0.009498356) {
                    if (input[8] < 0.037544537) {
                        if (input[1] < -0.03048607) {
                            if (input[2] < -0.03696189) {
                                var9 = 0.12616298;
                            } else {
                                var9 = -0.17922926;
                            }
                        } else {
                            if (input[2] < -0.017490756) {
                                if (input[5] < -0.0098818615) {
                                    var9 = 0.21962278;
                                } else {
                                    var9 = 0.01937822;
                                }
                            } else {
                                var9 = 0.007612662;
                            }
                        }
                    } else {
                        if (input[2] < -0.038976364) {
                            if (input[1] < -0.029159449) {
                                var9 = 0.22920059;
                            } else {
                                var9 = -0.068849646;
                            }
                        } else {
                            if (input[7] < 0.052617624) {
                                if (input[3] < -1.1753037) {
                                    if (input[6] < -0.91386044) {
                                        var9 = -0.19831847;
                                    } else {
                                        var9 = 0.073737204;
                                    }
                                } else {
                                    var9 = 0.17624615;
                                }
                            } else {
                                var9 = -0.17737642;
                            }
                        }
                    }
                } else {
                    var9 = -0.08817072;
                }
            } else {
                if (input[3] < -1.2242881) {
                    if (input[6] < -0.95542103) {
                        var9 = -0.06376391;
                    } else {
                        var9 = 0.24462736;
                    }
                } else {
                    if (input[6] < -0.9439412) {
                        var9 = -0.2682146;
                    } else {
                        if (input[2] < -0.027172506) {
                            var9 = -0.24860369;
                        } else {
                            if (input[8] < 0.034149013) {
                                if (input[4] < -0.011293441) {
                                    if (input[5] < -0.007539507) {
                                        if (input[7] < 0.046074547) {
                                            var9 = 0.20831084;
                                        } else {
                                            var9 = -0.052082226;
                                        }
                                    } else {
                                        var9 = -0.10727975;
                                    }
                                } else {
                                    var9 = -0.18594721;
                                }
                            } else {
                                if (input[4] < -0.01601803) {
                                    var9 = -0.12504208;
                                } else {
                                    var9 = 0.12581764;
                                }
                            }
                        }
                    }
                }
            }
        }
    } else {
        if (input[6] < -0.8579022) {
            if (input[0] < 2.1142607) {
                var9 = 0.2188978;
            } else {
                if (input[3] < -1.1753037) {
                    var9 = 0.2180712;
                } else {
                    var9 = -0.24524762;
                }
            }
        } else {
            var9 = 0.30384776;
        }
    }
    double var10;
    if (input[6] < -0.8579022) {
        if (input[6] < -0.9644232) {
            if (input[2] < -0.03318106) {
                var10 = 0.18288136;
            } else {
                var10 = -0.30007958;
            }
        } else {
            if (input[0] < 2.2558458) {
                if (input[6] < -0.9461092) {
                    var10 = -0.24561165;
                } else {
                    if (input[1] < -0.021331009) {
                        if (input[2] < -0.03696189) {
                            if (input[1] < -0.029159449) {
                                var10 = 0.22801277;
                            } else {
                                var10 = -0.037470143;
                            }
                        } else {
                            if (input[3] < -1.1235309) {
                                if (input[6] < -0.89921194) {
                                    if (input[4] < -0.012428386) {
                                        if (input[5] < -0.0064001516) {
                                            var10 = 0.25593427;
                                        } else {
                                            var10 = -0.07311615;
                                        }
                                    } else {
                                        if (input[3] < -1.178581) {
                                            var10 = -0.19276078;
                                        } else {
                                            if (input[7] < 0.045626514) {
                                                var10 = -0.10269184;
                                            } else {
                                                var10 = 0.20787838;
                                            }
                                        }
                                    }
                                } else {
                                    if (input[8] < 0.033006772) {
                                        var10 = 0.0638056;
                                    } else {
                                        if (input[1] < -0.037655555) {
                                            var10 = 0.052339215;
                                        } else {
                                            var10 = -0.19571859;
                                        }
                                    }
                                }
                            } else {
                                var10 = 0.17009795;
                            }
                        }
                    } else {
                        if (input[2] < -0.014123832) {
                            if (input[3] < -1.1913816) {
                                if (input[6] < -0.91386044) {
                                    if (input[3] < -1.2153419) {
                                        var10 = 0.15710393;
                                    } else {
                                        var10 = -0.29275045;
                                    }
                                } else {
                                    var10 = 0.17298266;
                                }
                            } else {
                                if (input[1] < -0.011652317) {
                                    if (input[5] < -0.007465656) {
                                        if (input[4] < -0.010273751) {
                                            var10 = 0.29236534;
                                        } else {
                                            var10 = 0.07818782;
                                        }
                                    } else {
                                        if (input[0] < 2.084277) {
                                            var10 = 0.14793183;
                                        } else {
                                            var10 = -0.13922916;
                                        }
                                    }
                                } else {
                                    var10 = -0.13387772;
                                }
                            }
                        } else {
                            if (input[6] < -0.8952168) {
                                var10 = -0.22626184;
                            } else {
                                if (input[3] < -1.049708) {
                                    var10 = 0.18654276;
                                } else {
                                    var10 = -0.19630231;
                                }
                            }
                        }
                    }
                }
            } else {
                if (input[4] < -0.015042401) {
                    if (input[3] < -1.2566861) {
                        var10 = -0.12808755;
                    } else {
                        if (input[7] < 0.041974068) {
                            var10 = -0.10370072;
                        } else {
                            var10 = 0.2023435;
                        }
                    }
                } else {
                    if (input[5] < -0.014499231) {
                        var10 = -0.052405074;
                    } else {
                        var10 = 0.2947298;
                    }
                }
            }
        }
    } else {
        var10 = 0.29959247;
    }
    double var11;
    if (input[6] < -0.8579022) {
        if (input[6] < -0.9644232) {
            if (input[2] < -0.03318106) {
                var11 = 0.16237716;
            } else {
                var11 = -0.2954243;
            }
        } else {
            if (input[2] < -0.017490756) {
                if (input[4] < -0.008413696) {
                    if (input[1] < -0.02682752) {
                        if (input[2] < -0.033784404) {
                            if (input[3] < -1.2566861) {
                                var11 = -0.13592027;
                            } else {
                                if (input[0] < 2.2244527) {
                                    var11 = 0.029476175;
                                } else {
                                    var11 = 0.25946838;
                                }
                            }
                        } else {
                            var11 = -0.14435849;
                        }
                    } else {
                        if (input[8] < 0.03768708) {
                            if (input[5] < -0.0098818615) {
                                if (input[2] < -0.031958528) {
                                    var11 = -0.030091349;
                                } else {
                                    if (input[4] < -0.016673163) {
                                        var11 = 0.0024932178;
                                    } else {
                                        var11 = 0.26539013;
                                    }
                                }
                            } else {
                                if (input[4] < -0.012357637) {
                                    var11 = 0.14078914;
                                } else {
                                    if (input[2] < -0.019927157) {
                                        var11 = -0.11379739;
                                    } else {
                                        var11 = 0.1607241;
                                    }
                                }
                            }
                        } else {
                            if (input[1] < -0.02315183) {
                                var11 = -0.17431028;
                            } else {
                                if (input[8] < 0.038856797) {
                                    var11 = -0.14001389;
                                } else {
                                    var11 = 0.1039853;
                                }
                            }
                        }
                    }
                } else {
                    if (input[8] < 0.03344659) {
                        var11 = -0.24465379;
                    } else {
                        var11 = 0.028951816;
                    }
                }
            } else {
                if (input[3] < -1.0963953) {
                    if (input[0] < 2.1662452) {
                        var11 = -0.19214556;
                    } else {
                        var11 = 0.041562;
                    }
                } else {
                    if (input[3] < -1.0463917) {
                        var11 = 0.2366196;
                    } else {
                        var11 = -0.19985531;
                    }
                }
            }
        }
    } else {
        var11 = 0.2954502;
    }
    double var12;
    if (input[6] < -0.8579022) {
        if (input[6] < -0.9644232) {
            if (input[2] < -0.03563804) {
                var12 = 0.17580087;
            } else {
                var12 = -0.28724563;
            }
        } else {
            if (input[2] < -0.014220504) {
                if (input[0] < 2.2542195) {
                    if (input[3] < -1.1900722) {
                        if (input[6] < -0.9192783) {
                            var12 = -0.22626555;
                        } else {
                            if (input[2] < -0.030552749) {
                                if (input[6] < -0.87337124) {
                                    if (input[0] < 2.2244527) {
                                        var12 = -0.19348927;
                                    } else {
                                        var12 = 0.12574328;
                                    }
                                } else {
                                    var12 = 0.17112076;
                                }
                            } else {
                                if (input[3] < -1.1956464) {
                                    if (input[3] < -1.2147261) {
                                        var12 = -0.004954702;
                                    } else {
                                        var12 = 0.290771;
                                    }
                                } else {
                                    var12 = -0.12974083;
                                }
                            }
                        }
                    } else {
                        if (input[6] < -0.9090667) {
                            if (input[7] < 0.03808883) {
                                var12 = -0.08940709;
                            } else {
                                var12 = 0.27103758;
                            }
                        } else {
                            if (input[1] < -0.02166582) {
                                if (input[0] < 2.1247864) {
                                    if (input[2] < -0.02375391) {
                                        var12 = 0.18965985;
                                    } else {
                                        var12 = -0.13902742;
                                    }
                                } else {
                                    var12 = -0.2281616;
                                }
                            } else {
                                if (input[2] < -0.019927157) {
                                    var12 = 0.24344684;
                                } else {
                                    if (input[7] < 0.045349758) {
                                        var12 = 0.17020997;
                                    } else {
                                        var12 = -0.13173963;
                                    }
                                }
                            }
                        }
                    }
                } else {
                    if (input[5] < -0.011162181) {
                        if (input[3] < -1.238215) {
                            if (input[6] < -0.9375794) {
                                var12 = -0.1360077;
                            } else {
                                var12 = 0.12365155;
                            }
                        } else {
                            var12 = 0.1925449;
                        }
                    } else {
                        var12 = 0.24006231;
                    }
                }
            } else {
                if (input[6] < -0.90158683) {
                    var12 = -0.25986305;
                } else {
                    if (input[3] < -1.1017689) {
                        var12 = -0.1317256;
                    } else {
                        if (input[3] < -1.0449692) {
                            var12 = 0.23678994;
                        } else {
                            var12 = -0.17330243;
                        }
                    }
                }
            }
        }
    } else {
        var12 = 0.2910836;
    }
    double var13;
    if (input[6] < -0.8579022) {
        if (input[7] < 0.03701756) {
            if (input[4] < -0.012637234) {
                if (input[1] < -0.02078901) {
                    var13 = 0.17369798;
                } else {
                    var13 = -0.08930321;
                }
            } else {
                var13 = -0.27615458;
            }
        } else {
            if (input[0] < 2.2288184) {
                if (input[6] < -0.9461092) {
                    var13 = -0.21006191;
                } else {
                    if (input[2] < -0.029493323) {
                        if (input[7] < 0.05160624) {
                            if (input[4] < -0.014409419) {
                                var13 = 0.19524758;
                            } else {
                                var13 = -0.12150261;
                            }
                        } else {
                            var13 = -0.17147407;
                        }
                    } else {
                        if (input[3] < -1.205431) {
                            var13 = 0.17817913;
                        } else {
                            if (input[0] < 2.1995862) {
                                if (input[6] < -0.92947114) {
                                    var13 = 0.2184243;
                                } else {
                                    if (input[8] < 0.029483538) {
                                        var13 = -0.15946352;
                                    } else {
                                        if (input[1] < -0.025132062) {
                                            if (input[4] < -0.011469043) {
                                                var13 = -0.18964824;
                                            } else {
                                                var13 = 0.102198616;
                                            }
                                        } else {
                                            if (input[5] < -0.016237462) {
                                                var13 = -0.17766199;
                                            } else {
                                                if (input[0] < 2.1755462) {
                                                    var13 = 0.1220958;
                                                } else {
                                                    var13 = -0.13245553;
                                                }
                                            }
                                        }
                                    }
                                }
                            } else {
                                var13 = -0.2532819;
                            }
                        }
                    }
                }
            } else {
                if (input[2] < -0.0197182) {
                    if (input[3] < -1.2522514) {
                        if (input[0] < 2.303829) {
                            var13 = 0.16467845;
                        } else {
                            var13 = -0.1316137;
                        }
                    } else {
                        var13 = 0.20830972;
                    }
                } else {
                    var13 = -0.08854614;
                }
            }
        }
    } else {
        var13 = 0.2861884;
    }
    double var14;
    if (input[6] < -0.86785334) {
        if (input[6] < -0.9784445) {
            var14 = -0.26149195;
        } else {
            if (input[5] < -0.009302213) {
                var14 = 0.031505805;
            } else {
                if (input[4] < -0.011109029) {
                    var14 = -0.020501079;
                } else {
                    if (input[0] < 2.1142607) {
                        var14 = -0.014055175;
                    } else {
                        var14 = -0.23035648;
                    }
                }
            }
        }
    } else {
        if (input[0] < 2.1142607) {
            var14 = 0.28018004;
        } else {
            if (input[3] < -1.1734661) {
                var14 = 0.21014039;
            } else {
                var14 = -0.17913863;
            }
        }
    }
    double var15;
    if (input[6] < -0.8579022) {
        if (input[4] < -0.008214228) {
            if (input[2] < -0.017490756) {
                if (input[8] < 0.037544537) {
                    var15 = 0.073780306;
                } else {
                    var15 = -0.031320654;
                }
            } else {
                if (input[0] < 2.0348344) {
                    if (input[3] < -1.0525924) {
                        var15 = 0.21693568;
                    } else {
                        var15 = -0.15084416;
                    }
                } else {
                    if (input[1] < -0.017411217) {
                        var15 = -0.0423097;
                    } else {
                        var15 = -0.21500657;
                    }
                }
            }
        } else {
            if (input[8] < 0.03358371) {
                var15 = -0.26245126;
            } else {
                var15 = 0.058331303;
            }
        }
    } else {
        var15 = 0.27391136;
    }
    double var16;
    if (input[6] < -0.8579022) {
        if (input[6] < -0.98452795) {
            var16 = -0.24780315;
        } else {
            if (input[5] < -0.007539507) {
                var16 = 0.01682799;
            } else {
                if (input[8] < 0.03142541) {
                    var16 = -0.21077466;
                } else {
                    var16 = -0.00014235737;
                }
            }
        }
    } else {
        var16 = 0.26593217;
    }
    double var17;
    if (input[6] < -0.8579022) {
        if (input[4] < -0.008013508) {
            if (input[1] < -0.018318295) {
                if (input[7] < 0.04978312) {
                    if (input[4] < -0.010790399) {
                        var17 = 0.11456648;
                    } else {
                        if (input[0] < 2.2591953) {
                            if (input[2] < -0.019489555) {
                                var17 = -0.2138441;
                            } else {
                                var17 = 0.067932576;
                            }
                        } else {
                            var17 = 0.16528395;
                        }
                    }
                } else {
                    if (input[0] < 2.2244527) {
                        if (input[3] < -1.160509) {
                            if (input[8] < 0.037544537) {
                                if (input[4] < -0.013395523) {
                                    var17 = 0.15284152;
                                } else {
                                    var17 = -0.12561817;
                                }
                            } else {
                                var17 = -0.18470022;
                            }
                        } else {
                            var17 = 0.09490787;
                        }
                    } else {
                        if (input[3] < -1.2490488) {
                            var17 = -0.095618226;
                        } else {
                            var17 = 0.22452436;
                        }
                    }
                }
            } else {
                if (input[6] < -0.9181448) {
                    var17 = -0.16999751;
                } else {
                    var17 = 0.0018288717;
                }
            }
        } else {
            if (input[6] < -0.8952168) {
                var17 = -0.22959292;
            } else {
                var17 = 0.099220976;
            }
        }
    } else {
        var17 = 0.25658405;
    }
    double var18;
    if (input[6] < -0.8579022) {
        if (input[6] < -0.9822939) {
            var18 = -0.2200034;
        } else {
            if (input[2] < -0.012197444) {
                if (input[0] < 2.0449388) {
                    var18 = 0.19908752;
                } else {
                    if (input[3] < -1.2229909) {
                        if (input[5] < -0.011162181) {
                            if (input[4] < -0.015323691) {
                                var18 = -0.093148306;
                            } else {
                                var18 = 0.08661035;
                            }
                        } else {
                            var18 = 0.17431979;
                        }
                    } else {
                        if (input[8] < 0.042523675) {
                            if (input[1] < -0.025132062) {
                                var18 = -0.15099242;
                            } else {
                                if (input[5] < -0.011560104) {
                                    if (input[0] < 2.0922506) {
                                        var18 = -0.12551033;
                                    } else {
                                        var18 = 0.13435188;
                                    }
                                } else {
                                    var18 = -0.056352794;
                                }
                            }
                        } else {
                            var18 = 0.14144596;
                        }
                    }
                }
            } else {
                var18 = -0.1476623;
            }
        }
    } else {
        var18 = 0.24586222;
    }
    double var19;
    if (input[6] < -0.86785334) {
        if (input[6] < -0.95408934) {
            if (input[2] < -0.03563804) {
                var19 = 0.16897164;
            } else {
                var19 = -0.18241677;
            }
        } else {
            if (input[0] < 2.235474) {
                var19 = -0.015273587;
            } else {
                if (input[0] < 2.3050196) {
                    var19 = 0.1967735;
                } else {
                    var19 = -0.09352741;
                }
            }
        }
    } else {
        var19 = 0.17600483;
    }
    double var20;
    if (input[0] < 2.0449388) {
        if (input[2] < -0.010803693) {
            var20 = 0.23528211;
        } else {
            var20 = -0.044127647;
        }
    } else {
        if (input[2] < -0.014220504) {
            if (input[2] < -0.038976364) {
                var20 = 0.14134347;
            } else {
                var20 = -0.010033196;
            }
        } else {
            var20 = -0.19911255;
        }
    }
    double var21;
    if (input[6] < -0.8579022) {
        if (input[7] < 0.03701756) {
            if (input[5] < -0.011985467) {
                var21 = 0.12379456;
            } else {
                var21 = -0.19540824;
            }
        } else {
            if (input[4] < -0.017901432) {
                var21 = -0.10272599;
            } else {
                if (input[5] < -0.014166867) {
                    var21 = -0.07891352;
                } else {
                    if (input[6] < -0.8839994) {
                        if (input[3] < -1.2229909) {
                            var21 = 0.1490089;
                        } else {
                            if (input[2] < -0.02921075) {
                                var21 = -0.17076074;
                            } else {
                                if (input[8] < 0.03142541) {
                                    var21 = -0.08280913;
                                } else {
                                    if (input[1] < -0.025940478) {
                                        var21 = -0.09641297;
                                    } else {
                                        var21 = 0.098397814;
                                    }
                                }
                            }
                        }
                    } else {
                        if (input[7] < 0.05494392) {
                            var21 = 0.2228387;
                        } else {
                            var21 = -0.044303402;
                        }
                    }
                }
            }
        }
    } else {
        var21 = 0.21211211;
    }
    double var22;
    if (input[6] < -0.9769194) {
        var22 = -0.17190102;
    } else {
        if (input[6] < -0.8579022) {
            var22 = 0.0040631527;
        } else {
            var22 = 0.19832256;
        }
    }
    double var23;
    if (input[5] < -0.007539507) {
        var23 = 0.02178545;
    } else {
        if (input[8] < 0.030183725) {
            var23 = -0.22110616;
        } else {
            var23 = 0.001990624;
        }
    }
    double var24;
    if (input[2] < -0.038976364) {
        var24 = 0.1306721;
    } else {
        if (input[6] < -0.9644232) {
            var24 = -0.17410758;
        } else {
            var24 = 0.00023514351;
        }
    }
    double var25;
    var25 = sigmoid(var0 + var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9 + var10 + var11 + var12 + var13 + var14 + var15 + var16 + var17 + var18 + var19 + var20 + var21 + var22 + var23 + var24 + -0.00040606665 + -0.0002864901 + -0.00020194186 + -0.00014275115 + -0.000100853846 + -0.00007078213 + -0.000050485178 + -0.00003544737 + -0.0000246644 + -0.000017592985 + -0.0000125383585 + -0.000008927495 + -0.00000636428 + -0.000004495122 + -0.000003203877 + -0.000002280948 + -0.000001623162 + -0.0000011646806 + -0.0000008383255 + -0.00000056614243 + -0.00000041562387 + -0.00000028137114 + -0.00000020283075 + -0.00000014748116 + -0.00000009871143 + -0.00000008891719 + -0.00000007682552 + -0.00000006755525 + -0.0000000598972 + -0.000000051553947 + -0.00000004865195 + -0.000000046233612 + -0.00000004462139 + -0.000000044298943 + -0.000000043815277 + -0.00000004188061 + -0.00000004026839 + -0.000000038978612 + -0.000000036882724 + -0.00000003591539 + -0.000000034464392 + -0.000000033174615 + -0.00000003269095 + -0.000000031562394 + -0.000000029788948 + -0.000000029305282 + -0.000000029144061 + -0.000000029144061 + -0.000000028821615 + -0.00000002769306 + -0.00000002769306 + -0.000000027048172 + -0.000000026242061 + -0.000000025597172 + -0.000000024952282 + -0.00000002398495 + -0.000000023662507 + -0.000000023662507 + -0.00000002317884 + -0.000000023017616 + -0.000000022695174 + -0.000000022050283 + -0.000000021889061 + -0.000000021566617 + -0.000000020921728 + -0.000000020599284 + -0.000000019954395 + -0.000000019793173 + -0.000000019470729 + -0.000000019470729 + -0.000000018503394 + -0.000000018180952 + -0.000000017213617 + -0.000000016891175 + -0.000000015923842);
    memcpy(output, (double[]){1.0 - var25, var25}, 2 * sizeof(double));
}
