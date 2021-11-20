/*!
 * WPBakery Page Builder v6.0.0 (https://wpbakery.com)
 * Copyright 2011-2021 Michael M, WPBakery
 * License: Commercial. More details: http://go.wpbakery.com/licensing
 */

// jscs:disable
// jshint ignore: start

!(function ($) {
    "use strict";
    function Carousel(element, options) {
        (this.$element = $(element)),
            (this.$indicators = this.$element.find(".vc_carousel-indicators")),
            (this.options = options),
            (this.paused = this.sliding = this.interval = this.$active = this.$items = null),
            "hover" === this.options.pause && this.$element.on("mouseenter", $.proxy(this.pause, this)).on("mouseleave", $.proxy(this.cycle, this)),
            this._build();
    }
    (Carousel.DEFAULTS = { mode: "horizontal", partial: !1, interval: 5e3, pause: "hover", wrap: !1, autoHeight: !1, perView: 1 }),
        (Carousel.prototype.cycle = function (e) {
            return (
                e || (this.paused = !1),
                this.interval && clearInterval(this.interval),
                this.options.interval && !this.paused && (this.interval = setInterval($.proxy(this.next, this), this.options.interval)),
                (this.touch_start_position = 0),
                this
            );
        }),
        (Carousel.prototype.getActiveIndex = function () {
            return (
                (this.$active = this.$element.find(".vc_item.vc_active")),
                this.$active.length || (this.$active = this.$element.find(".vc_item:first").addClass("vc_active")),
                (this.$items = this.$active.parent().children()),
                this.$items.index(this.$active)
            );
        }),
        (Carousel.prototype.showHideControl = function (index) {
            void 0 === index && (index = this.getActiveIndex()), this.$left_control[0 === index ? "hide" : "show"](), this.$right_control[index === this.items_count - 1 ? "hide" : "show"]();
        }),
        (Carousel.prototype.to = function (pos) {
            var that = this,
                activeIndex = this.getActiveIndex();
            if (!(pos > this.$items.length - 1 || pos < 0))
                return this.sliding
                    ? this.$element.one("slid", function () {
                          that.to(pos);
                      })
                    : activeIndex == pos
                    ? this.pause().cycle()
                    : this.slide(activeIndex < pos ? "next" : "prev", $(this.$items[pos]));
        }),
        (Carousel.prototype.pause = function (e) {
            return (
                e || (this.paused = !0),
                this.$element.find(".vc_right.vc_carousel-control, .vc_left.vc_carousel-control").length && $.support.transition.end && (this.$element.trigger($.support.transition.end), this.cycle(!0)),
                (this.interval = clearInterval(this.interval)),
                this
            );
        }),
        (Carousel.prototype.next = function () {
            if (!this.sliding) return this.slide("next");
        }),
        (Carousel.prototype.prev = function () {
            if (!this.sliding) return this.slide("prev");
        }),
        (Carousel.prototype.slide = function (type, fallback) {
            var $active = this.$element.find(".vc_item.vc_active"),
                $next = fallback || $active[type](),
                isCycling = this.interval,
                e = "next" === type ? "vc_left" : "vc_right",
                fallback = "next" === type ? "first" : "last",
                that = this;
            if (!$next.length) {
                if (!this.options.wrap) return void this.returnSwipedSlide();
                $next = this.$element.find(".vc_item")[fallback]();
            }
            (this.sliding = !0), isCycling && this.pause();
            e = $.Event("slide.vc.carousel", { relatedTarget: $next[0], direction: e });
            if (!$next.hasClass("vc_active")) {
                if (
                    (this.$indicators.length &&
                        (this.$indicators.find(".vc_active").removeClass("vc_active"),
                        this.$indicators.find(".vc_partial").removeClass("vc_partial"),
                        this.$element.one("slid", function () {
                            var index = that.getActiveIndex(),
                                $nextIndicator = $(that.$indicators.children().slice(index, that.getActiveIndex() + that.options.perView));
                            $nextIndicator && $nextIndicator.addClass("vc_active"),
                                that.options.partial && $nextIndicator && (index + 1 < that.items_count ? $nextIndicator.last().next() : $nextIndicator.first().prev()).addClass("vc_partial"),
                                that.options.wrap || that.showHideControl(index);
                        })),
                    (this.current_index = $next.index()),
                    that.options.wrap || this.showHideControl(this.current_index),
                    this.current_index > this.items_count ? (this.current_index = 0) : this.current_index < 0 && (this.current_index = this.items_count - 1),
                    this.options.autoHeight ? (this.current_pos_value = -1 * this._step * this.current_index) : (this.current_pos_value = -1 * $next.position()[this.animation_position]),
                    this.options.partial && this.current_index >= this.items_count - 1 && (this.current_pos_value += this._step * (1 - this.partial_part)),
                    $.support.transition && this.$element.hasClass("vc_slide"))
                ) {
                    if ((this.$element.trigger(e), e.isDefaultPrevented())) return;
                    this.$slideline_inner.addClass("vc_transition").css(this.animation_position, this.current_pos_value + that.pos_units),
                        this.options.autoHeight || this.recalculateSlidelineHeight($next.height(), !0),
                        this.$slideline_inner
                            .one($.support.transition.end, function () {
                                $next.addClass("vc_active"),
                                    $active.removeClass("vc_active"),
                                    that.$slideline_inner.removeClass([type, "vc_transition"].join(" ")),
                                    (that.sliding = !1),
                                    that.removeSwipeAnimationSpeed(),
                                    setTimeout(function () {
                                        that.$element.trigger("slid");
                                    }, 0);
                            })
                            .emulateTransitionEnd(this.transition_speed);
                } else {
                    if ((this.$element.trigger(e), e.isDefaultPrevented())) return;
                    $active.removeClass("vc_active"), $next.addClass("vc_active"), (this.sliding = !1), this.$slideline_inner.css(this.animation_position, this.current_pos_value + that.pos_units);
                }
                return isCycling && this.cycle(), this;
            }
        }),
        (Carousel.prototype.setSwipeAnimationSpeed = function () {
            this.$slideline_inner.addClass("vc_swipe-transition");
        }),
        (Carousel.prototype.removeSwipeAnimationSpeed = function () {
            this.$slideline_inner.removeClass("vc_swipe-transition");
        }),
        (Carousel.prototype.velocity = function (time, x) {
            return { x: Math.abs(x / time) || 0 };
        }),
        (Carousel.prototype.recalculateSlidelineHeight = function (height, animate) {
            !0 === animate ? this.$slideline.animate({ height: height }) : this.$slideline.height(height);
        }),
        (Carousel.prototype.resizeAction = function () {
            var new_slideline_height,
                max_height = 0;
            "horizontal" === this.options.mode && ((this.el_effect_size = this.$element.width() * (this.options.partial ? this.partial_part : 1)), this.$slideline.width(this.items_count * this.el_effect_size)),
                this.options.autoHeight
                    ? (this.$items.height("auto"),
                      this.$items.each(function () {
                          var item_height = $(this).height();
                          max_height < item_height && (max_height = item_height);
                      }),
                      this.$items.height(max_height))
                    : this.recalculateSlidelineHeight(this.$active.height()),
                "vertical" === this.options.mode &&
                    ((this._step = this.$active.height()),
                    (new_slideline_height = this.$active.height() * this.options.perView * (this.options.partial ? 2 - this.partial_part : 1)),
                    this.recalculateSlidelineHeight(new_slideline_height, !1),
                    this.$slideline_inner.css({ top: -1 * this.$active.position().top }),
                    (this.el_effect_size = this._step));
        }),
        (Carousel.prototype.returnSwipedSlide = function () {
            var params = {};
            (params[this.animation_position] = this.current_pos_value + this.pos_units), this.$slideline_inner.animate(params);
        }),
        (Carousel.prototype._build = function () {
            var el = this.$element.get(0),
                _touch_start_position = !1,
                _touch_start_time = 0,
                _pos_before_touch = 0,
                _diff = 0,
                _moved = !1,
                that = this,
                $active_indecators = this.options.mode;
            return (
                this.getActiveIndex(),
                (this.el_width = 0),
                (this.items_count = this.$items.length),
                (this.$slideline = this.$element.find(".vc_carousel-slideline")),
                (this.$slideline_inner = this.$slideline.find("> div")),
                (this.slideline_inner = this.$slideline_inner.get(0)),
                (this.partial_part = 0.8),
                (this._slide_width = 0),
                (this.swipe_velocity = 0.7),
                (this.current_pos_value = 0),
                (this.current_index = 0),
                (this.el_effect_size = 0),
                (this.transition_speed = 600),
                (this.$left_control = this.$element.find(".vc_left.vc_carousel-control")),
                (this.$right_control = this.$element.find(".vc_right.vc_carousel-control")),
                this.options.partial && (this.options.autoHeight = !0),
                1 < this.options.perView && this.$element.addClass("vc_per-view-more vc_per-view-" + this.options.perView),
                "horizontal" === $active_indecators
                    ? ((this.pos_units = "%"), (this._step = 100 / this.items_count / this.options.perView), (this.animation_position = "left"), this.$items.width(this._step + this.pos_units), (this.touch_direction = "pageX"))
                    : ((this.pos_units = "px"), (this.animation_position = "top"), (this.touch_direction = "pageY"), this.$element.addClass("vc_carousel_vertical")),
                that.options.wrap || this.showHideControl(),
                this.options.partial && this.$element.addClass("vc_partial"),
                this.$indicators.length &&
                    (($active_indecators = that.$indicators
                        .children()
                        .slice(this.current_index, this.current_index + this.options.perView)
                        .addClass("vc_active")),
                    this.options.partial && $active_indecators.last().next().addClass("vc_partial")),
                $(window).resize(this.resizeAction.bind(this)),
                this.resizeAction(),
                el.addEventListener(
                    "touchstart",
                    function (e) {
                        (_touch_start_position = parseFloat(e[that.touch_direction])), (_touch_start_time = e.timeStamp), (_pos_before_touch = that.$slideline_inner.position()[that.animation_position]);
                    }.bind(this),
                    !1
                ),
                el.addEventListener(
                    "touchmove",
                    function (e) {
                        return (
                            (_diff = parseFloat(e[that.touch_direction]) - _touch_start_position),
                            !(_moved = 0 < Math.abs(_diff)) || (e.preventDefault(), void (that.slideline_inner.style[that.animation_position] = _pos_before_touch + _diff + "px"))
                        );
                    },
                    !1
                ),
                el.addEventListener(
                    "touchend",
                    function (part) {
                        var velocity;
                        _moved &&
                            ((velocity = (part.timeStamp - _touch_start_time) / 1e3),
                            (part = _diff / that.el_effect_size),
                            ((velocity = that.velocity(velocity, part)).x > that.swipe_velocity && part < 0) || part <= -0.7
                                ? (that.setSwipeAnimationSpeed(), that.next())
                                : velocity.x > that.swipe_velocity || 0.7 <= part
                                ? (that.setSwipeAnimationSpeed(), that.prev())
                                : that.returnSwipedSlide(),
                            (_moved = !1));
                    },
                    !1
                ),
                this.$element.addClass("vc_build"),
                this
            );
        });
    var old = $.fn.carousel;
    ($.fn.carousel = function (option, value) {
        return this.each(function () {
            var $this = $(this),
                data = $this.data("vc.carousel"),
                options = $.extend({}, Carousel.DEFAULTS, $this.data(), "object" == typeof option && option),
                action = "string" == typeof option ? option : options.slide;
            data || ((data = new Carousel(this, options)), $this.data("vc.carousel", data)), "number" == typeof option ? data.to(option) : action ? data[action](value) : options.interval && data.pause().cycle();
        });
    }),
        ($.fn.carousel.Constructor = Carousel),
        ($.fn.carousel.noConflict = function () {
            return ($.fn.carousel = old), this;
        }),
        $(document)
            .off("click.vc.carousel.data-api")
            .on("click.vc.carousel.data-api", "[data-slide], [data-slide-to]", function (e) {
                var slideIndex = $(this),
                    $target = $(slideIndex.attr("data-target") || ((options = slideIndex.attr("href")) && options.replace(/.*(?=#[^\s]+$)/, ""))),
                    options = $.extend({}, $target.data(), slideIndex.data()),
                    slideIndex = slideIndex.attr("data-slide-to");
                slideIndex && (options.interval = !1), $target.carousel(options), slideIndex && $target.data("vc.carousel").to(slideIndex), e.preventDefault();
            }),
        $(document).ready(function () {
            console.log('??????')
            $('[data-ride="vc_carousel"]').each(function () {
                var $carousel = $(this);
                $carousel.carousel($carousel.data());
            });
        });
})(window.jQuery);
