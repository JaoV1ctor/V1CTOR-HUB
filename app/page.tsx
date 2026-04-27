'use client';

import Image from 'next/image';
import { motion } from 'motion/react';
import { 
  Briefcase, 
  Bot, 
  Monitor, 
  MessageCircle, 
  ArrowUpRight, 
  Github, 
  Linkedin, 
  Mail 
} from 'lucide-react';
import { cn } from '@/lib/utils';

const links = [
  {
    title: 'Portfólio de Projetos',
    url: 'https://jaov1ctors-portifolio.vercel.app/',
    icon: Briefcase,
    highlight: false,
    color: 'hover:text-blue-400',
    borderColor: 'hover:border-blue-400/50',
    bgHover: 'hover:bg-blue-400/10'
  },
  {
    title: 'Agentes de IA & Automações',
    url: `https://wa.me/5513991377983?text=${encodeURIComponent('Olá Jao! Gostaria de entender como um Agente de IA pode automatizar o atendimento da minha empresa.')}`,
    icon: Bot,
    highlight: false,
    color: 'hover:text-[#00A3FF]',
    borderColor: 'hover:border-[#00A3FF]/50',
    bgHover: 'hover:bg-[#00A3FF]/10'
  },
  {
    title: 'Sistemas Web & Landing Pages',
    url: `https://wa.me/5513991377983?text=${encodeURIComponent('Olá! Vi seu perfil e gostaria de um orçamento para um Site/Landing Page de alta performance.')}`,
    icon: Monitor,
    highlight: false,
    color: 'hover:text-indigo-400',
    borderColor: 'hover:border-indigo-400/50',
    bgHover: 'hover:bg-indigo-400/10'
  },
  {
    title: 'Agendar Consultoria Gratuita',
    url: `https://wa.me/5513991377983?text=${encodeURIComponent('Quero agendar meu diagnóstico gratuito de 15 minutos para avaliar a tecnologia da minha empresa.')}`,
    icon: MessageCircle,
    highlight: true,
  },
];

const socials = [
  { name: 'Github', url: 'https://github.com/JaoV1ctor', icon: Github },
  { name: 'LinkedIn', url: 'https://www.linkedin.com/in/joaovictormelo1/', icon: Linkedin },
  { name: 'Email', url: 'https://mail.google.com/mail/?view=cm&fs=1&to=vibeagency.oficial@gmail.com', icon: Mail },
];

export default function Home() {
  return (
    <main className="min-h-[100dvh] bg-[#050505] text-white flex flex-col relative overflow-x-hidden font-sans selection:bg-[#00A3FF]/30">
      
      {/* Fixed Ambient Backgrounds - Prevents stretching on mobile scrolling */}
      <div className="fixed inset-0 pointer-events-none z-0">
        <div className="absolute top-[-10%] left-[-10%] w-[300px] h-[300px] md:w-[600px] md:h-[600px] bg-blue-600/15 rounded-full blur-[80px] md:blur-[120px]" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[300px] h-[300px] md:w-[600px] md:h-[600px] bg-[#00A3FF]/15 rounded-full blur-[80px] md:blur-[120px]" />
        
        {/* Subtle Grid Overlay */}
        <div 
          className="absolute inset-0 opacity-[0.03]" 
          style={{ backgroundImage: 'radial-gradient(#fff 1px, transparent 1px)', backgroundSize: '40px 40px' }} 
        />

        {/* Background Geometric Accents - Responsive scaling */}
        <div className="hidden sm:block absolute left-5 md:left-20 top-10 md:top-40 w-8 h-8 md:w-12 md:h-12 border-t border-l border-white/10" />
        <div className="hidden sm:block absolute right-5 md:right-20 bottom-10 md:bottom-40 w-8 h-8 md:w-12 md:h-12 border-b border-r border-white/10" />
        
        {/* Dynamic Typography Backgrounds */}
        <div className="absolute right-[5%] md:right-[15%] top-[10%] md:top-[20%] text-4xl sm:text-6xl md:text-[80px] font-black text-white/[0.02] select-none">ARTIFICIAL</div>
        <div className="absolute left-[5%] md:left-[15%] bottom-[10%] md:bottom-[15%] text-4xl sm:text-6xl md:text-[80px] font-black text-white/[0.02] select-none">AUTOMATION</div>
      </div>

      {/* Content Container - Uses my-auto to allow responsive vertical scrolling without cutting top content */}
      <div className="flex-1 flex flex-col items-center justify-center w-full min-h-[100dvh] px-4 py-12 sm:px-8 sm:py-16 md:p-12 z-10">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          className="w-full max-w-[100%] sm:max-w-md md:max-w-xl lg:max-w-2xl bg-white/5 backdrop-blur-2xl rounded-[32px] sm:rounded-[48px] border border-white/10 shadow-[0_16px_40px_rgba(0,0,0,0.5)] md:shadow-[0_32px_64px_rgba(0,0,0,0.8)] relative flex flex-col items-center px-4 py-8 sm:px-8 sm:py-12 md:px-14 md:py-14 my-auto"
        >
          {/* Profile Picture */}
          <motion.div 
            initial={{ scale: 0.8, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
            className="relative mb-6 sm:mb-8 group"
          >
            {/* Pulsating Blue Ring Outside */}
            <div className="absolute -inset-3 rounded-full border border-[#00A3FF]/40 animate-[pulse_2s_ease-in-out_infinite] shadow-[0_0_15px_rgba(0,163,255,0.3)] md:shadow-[0_0_20px_rgba(0,163,255,0.3)] pointer-events-none" />
            <div className="absolute -inset-1.5 rounded-full border border-[#00A3FF]/60 animate-[pulse_3s_ease-in-out_infinite] pointer-events-none" />
            
            <div className="relative w-28 h-28 sm:w-32 sm:h-32 md:w-40 md:h-40 rounded-full border-2 border-[#00A3FF] p-0.5 flex items-center justify-center bg-transparent shadow-[0_0_20px_rgba(0,163,255,0.4)] md:shadow-[0_0_40px_rgba(0,163,255,0.4)] z-10">
              <div className="w-full h-full rounded-full overflow-hidden flex items-center justify-center">
                <Image 
                  src="/logo.png" 
                  alt="Logo JaoV1ctor"
                  width={256}
                  height={256}
                  className="w-full h-full object-contain transition-transform duration-700 group-hover:scale-110"
                  referrerPolicy="no-referrer"
                />
              </div>
            </div>
          </motion.div>

          {/* Name & Bio */}
          <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
            className="text-center mb-8 sm:mb-10 w-full"
          >
            <h1 className="text-xl sm:text-[26px] md:text-3xl font-bold tracking-tight text-white flex flex-col sm:flex-row items-center justify-center gap-2 sm:gap-3 md:gap-4 mb-3 sm:mb-4">
              JaoV1ctor 
              <span className="hidden sm:inline-block text-[#00A3FF] font-light text-[22px] sm:text-[26px] md:text-3xl">|</span> 
              <span className="text-zinc-200 font-medium text-[14px] sm:text-[18px] md:text-[20px] mt-1 sm:mt-0">Automação & IA</span>
            </h1>
            <p className="text-gray-400 text-xs sm:text-sm md:text-base leading-relaxed px-2 font-medium max-w-[280px] sm:max-w-[320px] md:max-w-[400px] mx-auto">
              Escalando negócios através de Inteligência Artificial e Automação.
            </p>
          </motion.div>

          {/* Links */}
          <div className="w-full flex flex-col gap-3 sm:gap-4">
            {links.map((link, index) => (
              <motion.a
                key={link.title}
                href={link.url}
                target="_blank"
                rel="noopener noreferrer"
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.3 + index * 0.1, ease: [0.16, 1, 0.3, 1] }}
                className={cn(
                  "group relative flex items-center justify-between p-3.5 px-4 sm:p-4 sm:px-6 md:p-5 md:px-8 rounded-xl sm:rounded-2xl transition-all duration-500 overflow-hidden outline-none",
                  link.highlight 
                    ? "bg-gradient-to-r from-[#00A3FF] to-[#0077FF] border border-transparent shadow-[0_0_15px_rgba(0,163,255,0.3)] md:shadow-[0_0_20px_rgba(0,163,255,0.4)] hover:shadow-[0_0_35px_rgba(0,163,255,0.7)] hover:-translate-y-1 hover:scale-[1.01]" 
                    : cn(
                        "bg-white/[0.02] border border-white/5 hover:border-transparent hover:-translate-y-1 hover:shadow-lg",
                        link.borderColor,
                        link.bgHover
                      )
                )}
              >
                {/* Highlight background shine effect on hover */}
                {link.highlight && (
                  <div className="absolute top-0 left-0 w-[200%] h-full bg-gradient-to-r from-transparent via-white/30 to-transparent -skew-x-12 -translate-x-[150%] group-hover:translate-x-[50%] transition-transform duration-1000 pointer-events-none" />
                )}
                
                {/* Normal card ambient glow */}
                {!link.highlight && (
                   <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 bg-gradient-to-r from-transparent via-white/5 to-transparent pointer-events-none" />
                )}

                <div className="flex items-center gap-3 sm:gap-4 z-10 w-full">
                  <div className={cn(
                    "transition-all duration-500 flex-shrink-0 transform group-hover:scale-125 group-hover:-rotate-6",
                    link.highlight 
                      ? "text-[#050505]" 
                      : cn("text-gray-400 drop-shadow-none group-hover:drop-shadow-[0_0_8px_currentColor]", link.color)
                  )}>
                    <link.icon size={20} strokeWidth={2} className="sm:w-[22px] sm:h-[22px]" />
                  </div>
                  <span className={cn(
                    "text-[12px] sm:text-[14px] md:text-[15px] transition-colors duration-300 text-left w-full",
                    link.highlight ? "font-bold text-[#050505]" : "font-semibold text-gray-200 group-hover:text-white"
                  )}>
                    {link.title}
                  </span>
                </div>
                
                {/* Arrow Icon */}
                <div className={cn(
                  "z-10 transform group-hover:translate-x-1 group-hover:-translate-y-1 transition-all duration-300 flex-shrink-0",
                  link.highlight ? "text-[#050505]" : cn("text-gray-600", link.color)
                )}>
                  <ArrowUpRight size={18} strokeWidth={2.5} className="sm:w-[20px] sm:h-[20px]" />
                </div>
              </motion.a>
            ))}
          </div>

          {/* Social Icons */}
          <motion.div 
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8, delay: 0.7, ease: [0.16, 1, 0.3, 1] }}
            className="flex items-center justify-center gap-3 sm:gap-4 mt-8 md:mt-10"
          >
            {socials.map((social, idx) => (
              <a 
                key={social.name} 
                href={social.url}
                target="_blank"
                rel="noopener noreferrer"
                className="group p-2.5 sm:p-3 rounded-full bg-white/[0.02] border border-white/5 text-gray-400 hover:text-[#00A3FF] hover:bg-[#00A3FF]/10 hover:border-[#00A3FF]/50 transition-all duration-300 hover:scale-110 hover:-translate-y-1 shadow-lg overflow-hidden relative"
                aria-label={social.name}
              >
                {/* Subtle shine on social button */}
                <div className="absolute inset-0 bg-white/20 -translate-y-full group-hover:translate-y-full transition-transform duration-500 opacity-0 group-hover:opacity-100 pointer-events-none" />
                <social.icon size={16} strokeWidth={2} className="relative z-10 transition-transform duration-300 group-hover:rotate-12 group-hover:drop-shadow-[0_0_6px_rgba(0,163,255,0.8)] sm:w-[18px] sm:h-[18px]" />
              </a>
            ))}
          </motion.div>

          {/* Footer */}
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.8 }}
            className="mt-8 sm:mt-10 flex flex-col items-center gap-3 w-full"
          >
            <div className="w-10 sm:w-12 h-[1px] bg-white/10" />
            <div className="flex flex-col items-center gap-1">
              <span className="text-zinc-400 text-[10px] sm:text-[11px] font-medium tracking-wider">
                {new Date().getFullYear()} © JaoV1ctor.
              </span>
              <span className="text-zinc-600 text-[8px] sm:text-[9px] font-bold tracking-[0.2em] uppercase">
                {"// Engineered with AI"}
              </span>
            </div>
          </motion.div>
        </motion.div>
      </div>
    </main>
  );
}
